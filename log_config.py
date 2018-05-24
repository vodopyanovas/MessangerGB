import logging
import sys

def test_func1():
    log.debug('This message is from function')
    log.info('Info message')
    log.critical('CRITICAAAAL!!!')

def test_func2():
    pass


log = logging.getLogger(__name__)

# Setting logging level
log.setLevel(logging.DEBUG)

# Set log message format
# <datetime> <level> <module name> <function call name> <message>
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')

# Adding handler for writing log to file
log_handler = logging.FileHandler('app.log')
log_handler.setLevel(logging.DEBUG)
log_handler.setFormatter(formatter)

# Adding handler for writing log to console
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

log.addHandler(log_handler)
log.addHandler(stream_handler)



test_func1()







# Основное задание:
# ● Реализовать логгирование с использованием модуля logging:
# ○ Реализовать декоратор @log, фиксирующий обращение к декорируемой функции:
# сохраняет имя функции и её аргументы.
# ○ Настройку логгера выполнить в отдельном модуле log_config.py:
# ● Создание именованного логгера.
# ● Сообщения лога должны иметь следующий формат:
# "<дата-время> <уровень_важности> <имя_модуля> <имя_функции> <сообщение>"
# ● Журналирование должно производиться в лог-файл.
# ● На стороне сервера необходимо настроить ежедневную ротацию лог-файлов
# ● Реализовать обработку нескольких клиентов на сервере с использованием
# функции select таким образом, что клиенты общаются в "общем чате", т.е.
# каждое сообщение каждого клиента отправляется всем клиентам,
# подключенным к серверу.
# ● Реализовать функции отправки/приёма данных на стороне клиента. Для
# упрощения разработки приложения на данном этапе пусть клиентское
# приложение будет либо только принимать, либо только отправлять сообщения в
# общий чат:
# ● запуск скрипта клиента должен осуществляться с параметром командной
# строки: -r (чтение чата) или -w (передача сообщений в чат).
# ● Для всех функций необходимо написать тесты.

# В декораторе @log реализовать фиксацию функции, из которой была вызвана декорированная
# функция. Т.е

# То в логе должна быть отражена информация:
# "<дата-время> Функция func_z() вызвана из функции main"
