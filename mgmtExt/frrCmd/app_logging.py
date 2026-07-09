import logging
import logging.handlers
import sys

class Logging(object):
    def __init__(self):
        # Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
        logging.getLogger().setLevel(logging.NOTSET)

        FORMAT = '[%(levelname)s][%(filename)s:%(lineno)s.%(funcName)s()]: %(message)s'
        # Add stdout handler, with level INFO
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        formater = logging.Formatter(FORMAT, "%Y-%m-%d %H:%M:%S")
        console.setFormatter(formater)
        logging.getLogger().addHandler(console)

        # Add file rotating handler, with level DEBUG
        rotatingHandler = logging.handlers.RotatingFileHandler(
            filename='logs/decmd.log', maxBytes=3000000, backupCount=5)
        rotatingHandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FORMAT)
        rotatingHandler.setFormatter(formatter)
        logging.getLogger().addHandler(rotatingHandler)
        self.LOG = logging.getLogger("app." + __name__)

    def getLogger(self):
        return self.LOG
        
LOG = Logging().getLogger()