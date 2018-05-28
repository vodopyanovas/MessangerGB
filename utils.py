import json
import time
import sys
import argparse


def timestamp():
    unix_time = time.time()
    return int(unix_time)


def encode_json(message):
    to_json = json.dumps(message)
    to_json_b = to_json.encode('utf-8')
    return to_json_b


def decode_json(message):
    decode = message.decode('utf-8')
    to_dict = json.loads(decode)
    return to_dict


def arg_parser():
    parser = argparse.ArgumentParser(
        prog='JIM-ME Messanger',
        description='JSON based Instant messanger',
        epilog='(c) AntonVo 2018.',
        add_help=False
    )
    parser_group = parser.add_argument_group(title='Parameters')
    parser_group.add_argument ('--help', '-h', action='help', help='Help')

    parser_group.add_argument('--addr', '-a', help='IP address')
    parser_group.add_argument('--port', '-p', type=int, default=7777, help='TCP port')

    return parser
