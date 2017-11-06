import logging
import time

from logging.handlers import RotatingFileHandler


# ----------------------------------------------------------------------
def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    loghandler = RotatingFileHandler('testLog', maxBytes=10000, backupCount=0)
    logger.addHandler(loghandler)

    print('created Log file')
    logging.info('Logging starts ...')

    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=2000,
                                  backupCount=0)
    #logger.addHandler(handler)


    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "test.log"
    create_rotating_log(log_file)