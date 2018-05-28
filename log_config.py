import logging
from logging.handlers import TimedRotatingFileHandler
import sys


def log(func):
    def callf(*args, **kwargs):
        # Containes function from which was called
        call_log = sys._getframe(1).f_code.co_name
        app_log.debug(f'Function {func.__name__}: args:{args}, kwargs:{kwargs}, called by: {call_log}')
        return func(*args, **kwargs)
    return callf


app_log = logging.getLogger('app')

# Setting logging level
app_log.setLevel(logging.DEBUG)

# Set log message format
# <datetime> <level> <module name> <function call name> <message>
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')

# Adding handler for writing log to file with each day file rotating
log_handler = TimedRotatingFileHandler(f'app.log', backupCount=7, when='D', interval=1)
log_handler.setLevel(logging.DEBUG)
log_handler.setFormatter(formatter)


# Adding handler for writing log to console
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(logging.CRITICAL)
stream_handler.setFormatter(formatter)

app_log.addHandler(log_handler)
app_log.addHandler(stream_handler)
