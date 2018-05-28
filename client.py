# Messanger client
from socket import socket, AF_INET, SOCK_STREAM
import logging
import sys

from jim import presence
from utils import timestamp, encode_json, decode_json, arg_parser
import log_config


app_log = logging.getLogger('app')


def log(func):
    def callf(*args, **kwargs):
        # Containes function from which was called
        call_log = sys._getframe(1).f_code.co_name
        app_log.debug(f'function:{func.__name__}: args:{args}, kwargs:{kwargs}, called by: {call_log}')
        return func(*args, **kwargs)
    return callf


@log
def start_client(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)
    return sock


def cli_loop(message):
    address = (HOST, PORT)
    sock = start_client(address)
    sock.send(message)
    data = sock.recv(1024)
    print(decode_json(data))


presence_msg = encode_json(
    presence('Anton', status="online")
)

# имеет параметры командной строки:
# -p --port <port> - TCP-порт для работы (по умолчанию использует порт 7777)
# -a --addr <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)

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

    cli_loop(presence_msg)
