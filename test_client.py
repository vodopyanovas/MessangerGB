import pytest
import socket
from subprocess import Popen, CREATE_NEW_CONSOLE
from client import start_client


def test_start_client_1():
    try:
        sock = start_client(('localhost', 7777))
    except OSError as e:
        print('\nThe server is not running')
        print('Starting server')
        p = Popen('py server.py', creationflags=CREATE_NEW_CONSOLE)

        try:
            sock = start_client(('localhost', 7777))
        except Exception as e:
            print(e)
        finally:
            p.kill()
            print('Server shutdown')

    finally:
        assert isinstance(sock, socket.socket)
