import logging
import logging.handlers
import sys
from datetime import datetime

class Logging(object):
    def __init__(self, node):
        # Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
        logger = logging.getLogger()
        logger.setLevel(logging.NOTSET)

        FORMAT = '%(message)s'
        # Add stdout handler, with level INFO
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        formater = logging.Formatter(FORMAT, "%Y-%m-%d %H:%M:%S")
        console.setFormatter(formater)
        logger.addHandler(console)

        # Add file rotating handler, with level DEBUG
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        rotatingHandler = logging.handlers.RotatingFileHandler(
            filename=f'frrCmdTester_{node}_{timestamp}.rst', maxBytes=3000000, backupCount=5)
        rotatingHandler.setLevel(logging.INFO)
        formatter = logging.Formatter(FORMAT)
        rotatingHandler.setFormatter(formatter)
        logger.addHandler(rotatingHandler)
        self.LOG = logger

    def getLogger(self):
        return self.LOG
        