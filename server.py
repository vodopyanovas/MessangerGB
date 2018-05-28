
# Messanger server
from socket import socket, AF_INET, SOCK_STREAM
import logging
import sys
import select

from utils import timestamp, encode_json, decode_json, arg_parser
from jim import response
import log_config
# from log_config import log


app_log = logging.getLogger('app')

def log(func):
    def callf(*args, **kwargs):
        # Containes function from which was called
        call_log = sys._getframe(1).f_code.co_name
        app_log.debug(f'function:{func.__name__}: args:{args}, kwargs:{kwargs}, called by: {call_log}')
        return func(*args, **kwargs)
    return callf

@log
def start_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2)
    return sock

def srv_loop():
    address = (HOST, PORT)
    clients = []
    sock = start_server(address)

    while True:
        try:
            client, address = sock.accept()
        except OSError as e:
            pass
        else:
            print(f'Connected with {str(address)}')
            clients.append(client)
        finally:
            w = []
            try:
                r, w, e = select.select([], clients, [], 0)
            except Exception as e:
                pass

        for s_client in w:
            srv_response = encode_json(response(200))
            try:
                data = s_client.recv(1024)
                print(decode_json(data))
                s_client.send(srv_response)
            except:
                clients.remove(s_client)


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
    srv_loop()




# имеет параметры командной строки:
# -p --port <port> - TCP-порт для работы (по умолчанию использует порт 7777)
# -a --addr <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)
