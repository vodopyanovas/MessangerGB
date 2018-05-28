# message types description

from utils import timestamp

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

# presense message
def presence(account, status=''):
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

# server response
def response(code):
    if code < 400:
        msg = {
            'response': code,
            'time': timestamp(),
            'alert': RESPONSE_CODE[code],
            'error' : ''
        }
    else:
        msg = {
            'response': code,
            'time': timestamp(),
            'alert': '',
            'error' : ERROR_CODE[code]
        }
    return msg





