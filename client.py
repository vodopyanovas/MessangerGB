

# Messanger client
from socket import socket, AF_INET, SOCK_STREAM

from jim import presence_msg
from utils import timestamp, encode_json, decode_json, arg_parser


def main(HOST, PORT, message):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))   # Соединиться с сервером
        s.sendall(message)
        data = s.recv(1024)
    print(decode_json(data))

presence_msg = encode_json(
    presence_msg(timestamp(), 'Anton', status="online")
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

    main(HOST, PORT, presence_msg)
