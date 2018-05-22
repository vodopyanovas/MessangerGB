import pytest
from utils import encode_json, decode_json

def test_encode_json():
    assert isinstance(encode_json({'a': 1, 'b': 'string'}), bytes)

def test_decode_json():
    assert isinstance(decode_json(b'{"a": 1, "b": "string"}'), dict)
