'''Class for handling the logs '''

import logging
from logging.handlers import RotatingFileHandler
class Log():
    def __init__(self, logfile):
        self._logger = logging.getLogger("Rotating Log")
        self._logger.setLevel(logging.INFO)
        loghandler = RotatingFileHandler(logfile, maxBytes=10000, backupCount=0)
        self._logger.addHandler(loghandler)

    def log(self, record):
        if len(record) > 0:
            self._logger.info(record)


'''
from flask_restful import Resource
logfile = "helloworldlogs.log"

count = dict()
class GetLog(Resource):
    def get(self):
        t = ''
        with open("helloworldlogs.log") as f:
            t = f.readlines()
            for i in t:
                ip = i.split('|')[0].strip()
                count[ip] = count.get(ip, 0) + 1
        print(count)
        return t
'''

def get_circular_logger(filename):
    logger = Log(filename)
    return logger