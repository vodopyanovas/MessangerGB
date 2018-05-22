

# message types description

# presense message
def presence_msg(unix_time, account, status=''):
    msg = {
        "action": "presence",
        "time": unix_time,
        "type": "status" ,
        "user": {
            "account_name": account,
            "status": status
        }
    }
    return msg

# server response
def response(code, unix_time, message, error=''):
    msg = {
        'response': code,
        'time': unix_time,
         'alert': message,
         'error' : error
         }
    return msg
