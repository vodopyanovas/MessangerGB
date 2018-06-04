# message types description

from utils import timestamp


class JIMMessage:

    def presence(self, account, status=''):
        msg = {
            "action": "presence",
            "time": timestamp(),
            "type": "status" ,
            "user": {
                "account_name": account,
                "status": status
            }
        }
        return msg

    def authenticate(self, account, password):
        msg = {
            "action": "authenticate",
            "time": timestamp(),
            "user": {
                "account_name": account,
                "password": password
            }
        }
        return msg

    def message(self, msg_to, msg_from, message):
        msg = {
            "action": "msg",
            "time": timestamp(),
            "to": msg_to,
            "from": msg_from,
            "encoding": "utf-8",
            "message": message
        }
        return msg

    def group_msg(self, msg_to, msg_from, message):
        msg = {
            "action": "msg",
            "time": timestamp(),
            "to": '#' + msg_to,
            "from": msg_from,
            "encoding": "utf-8",
            "message": message
        }
        return msg

    def join_chat(self, room_name):
        msg = {
            "action": "join",
            "time": timestamp(),
            "room": '#' + room_name
        }
        return msg

    def leave_chat(self, room_name):
        msg = {
            "action": "leave",
            "time": timestamp(),
            "room": '#' + room_name
        }
        return msg

class JIMResponse:

    RESPONSE_CODE = {
    100: 'NOTIFICATION',
    101: 'IMPORTANT NOTIFICATION',
    200: 'OK',
    201: 'OBJECT CREATED',
    202: 'ACCEPTED'
    }

    ERROR_CODE = {
        400: 'ERROR: WRONG REQUEST',
        401: 'ERROR: NOT AUTHORISED',
        402: 'ERROR: BAD CREDENTIALS',
        403: 'ERROR: FORBIDDEN',
        404: 'ERROR: NOT FOUND',
        409: 'ERROR: LOGIN CONFLICT',
        410: 'ERROR: USER OFFLINE',
        500: 'SERVER ERROR'
    }

    def response(self, code):
        if code < 400:
            msg = {
                'response': code,
                'time': timestamp(),
                'alert': self.RESPONSE_CODE[code]
            }
        else:
            msg = {
                'response': code,
                'time': timestamp(),
                'error' : self.ERROR_CODE[code]
            }
        return msg

# message = JIMMessage()
# response = JIMResponse()


# print(message.presence('anton', status='online'))
# print(message.authenticate('anton', '12345'))
# print(message.message('timur','anton', 'Hello World!'))
# print(message.group_msg('group chat','anton', 'Hello World!'))
# print(message.join_chat('group chat'))
# print(message.leave_chat('group chat'))


# print(response.response(200))
# print(response.response(400))
