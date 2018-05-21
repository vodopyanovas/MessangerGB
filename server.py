
# Messanger server
from socket import socket, AF_INET, SOCK_STREAM

from utils import timestamp, encode_json, decode_json, arg_parser
from jim import response


def main(HOST, PORT):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        while True:
            client, addr = s.accept()
            with client:
                print(f"Connected by {str(addr)}")
                data = client.recv(1024)
                if not data: break
                print(decode_json(data))
                client.send(
                    encode_json(
                        response(200, timestamp(), 'OK')
                    )
                )


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

    main(HOST, PORT)

# имеет параметры командной строки:
# -p --port <port> - TCP-порт для работы (по умолчанию использует порт 7777)
# -a --addr <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)

# Поддерживаемые коды ошибок:
# 0xx - информационные сообщения:
#     100 - базовое уведомление;
#     101 - важное уведомление.
# 2xx - успешное завершение:
#     200 - OK;
#     201 (created) - объект создан;
#     202 (accepted)- подтверждение.
# 4xx - ошибка на стороне клиента:
#     400 - неправильный запрос/JSON-объект;
#     401 - не авторизован;
#     402 - неправильный логин/пароль;
#     403 (forbidden) - пользователь заблокирован;
#     404 (not found) - пользователь/чат отсутствует на сервере;
#     409 (conflict) - уже имеется подключение с указанным логином;
#     410 (gone) - адресат существует, но недоступен (offline).
# 5xx - ошибка на стороне сервера:
#     500 - ошибка сервера
