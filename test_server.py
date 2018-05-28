import pytest
import socket
from server import start_server


def test_start_server_1():
    sock = start_server(('', 7777))
    assert isinstance(sock, socket.socket)
