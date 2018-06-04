
# Messanger server
from socket import socket, AF_INET, SOCK_STREAM
import logging
import select

from utils import timestamp, encode_json, decode_json, arg_parser
from jim import JIMResponse
import log_config
from log_config import log


app_log = logging.getLogger('app')

response = JIMResponse()


class JIMServer:

    def __init__(self):
        self.clients = []

    def start_server(self):
        address = (HOST, PORT)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(address)
        sock.listen(5)
        sock.settimeout(0.2)
        return sock

    def get_client(self, sock):
        try:
            client, address = sock.accept()
        except OSError as e:
            pass
        else:
            print(f'Connected with {str(address)}')
            self.clients.append(client)
        finally:
            w = []
            try:
                r, w, e = select.select([], self.clients, [], 0)
            except Exception as ex:
                pass
        return w

    def parse_msg(self, data):
        print(data)
        action = data['action']
        if action == 'authenticate':
            print('Checking auth params...')
            check = 1
            if check:
                return 202, action
            else:
                return 402, action
        elif action == 'presence':
            # print('Presense message!')
            return 200, action
        elif action == 'msg':
            print(f'Message to: {data["to"]}')
            return 200, action, data["to"]
        elif action == 'join':
            # print('Join')
            return 200, action
        elif action == 'leave':
            # print('Leave')
            return 200, action
        elif action == 'quit':
            # print('Quit')
            return 200, action


    def get_data(self, client_socket):
        for s_client in client_socket:
            try:
                data = s_client.recv(1024)
                decoded_data = decode_json(data)
                parsed_data = self.parse_msg(decoded_data)
                send_response = encode_json(response.response(parsed_data[0]))

                # print(parsed_data[1])
                s_client.send(send_response)
            except:
                self.clients.remove(s_client)

    def server_loop(self):
        sock = self.start_server()

        while True:
            w = self.get_client(sock)
            self.get_data(w)

    def probe(self):
        msg = {
            "action": "probe",
            "time": timestamp()
        }
        return msg


if __name__ == '__main__':
    parser = arg_parser()
    namespace = parser.parse_args()

    if namespace.addr:
        HOST = namespace.addr
        PORT = namespace.port
    elif namespace.port:
        HOST = ''
        PORT = namespace.port
    else:
        HOST = ''
        PORT = 7777

    print('Server started')

    server = JIMServer()
    server.server_loop()


# имеет параметры командной строки:
# -p --port <port> - TCP-порт для работы (по умолчанию использует порт 7777)
# -a --addr <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)
