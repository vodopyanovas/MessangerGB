import pytest
from jim import presence, response, RESPONSE_CODE, ERROR_CODE

def test_response_1():
    msg = response(200)
    assert msg['response'] == 200
    assert msg['alert'] == RESPONSE_CODE[200]

def test_response_2():
    msg = response(400)
    assert msg['response'] == 400
    assert msg['alert'] == ''
    assert msg['error'] == ERROR_CODE[400]

def test_presence():
    msg = presence('Anton', 'online')
    assert msg['action'] == 'presence'
    assert msg['user']['account_name'] == 'Anton'
    assert msg['user']['status'] == 'online'
