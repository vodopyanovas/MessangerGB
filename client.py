# Messanger client

# имеет параметры командной строки:
# -p --port <port> - TCP-порт для работы (по умолчанию использует порт 7777)
# -a --addr <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)

from socket import socket, AF_INET, SOCK_STREAM
import logging

from jim import JIMMessage
from utils import encode_json, decode_json, arg_parser
import log_config
from log_config import log


app_log = logging.getLogger('app')

msg = JIMMessage()


class JIMClient:

    def __init__(self, account, password):
        self.account = account
        self.password = password

    def start_client(self):
        address = (HOST, PORT)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(address)
        return sock

    def send_msg(self, *args):
        sock = self.start_client()
        for arg in args:
            msg = encode_json(arg)
            sock.send(msg)
            data = sock.recv(1024)
            decoded_data = decode_json(data)
            print(decode_json(decoded_data))


if __name__ == '__main__':
    parser = arg_parser()
    namespace = parser.parse_args()

    if namespace.addr:
        HOST = namespace.addr
        PORT = namespace.port
    elif namespace.port:
        HOST = 'localhost'
        PORT = namespace.port
    else:
        HOST = 'localhost'
        PORT = 7777


    user = JIMClient('anton', '12345')

    auth_msg = msg.authenticate(user.account, user.password)
    presence_msg = msg.presence(user.account, status='online')

    msg_text = 'Привет! Как твои дела? Чего нового?'
    message = msg.message('Timur', user.account, msg_text)

    # user.send_msg(auth_msg, presence_msg, message)
    user.send_msg(message)
