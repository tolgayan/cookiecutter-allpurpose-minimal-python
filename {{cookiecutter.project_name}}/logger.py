import datetime
import logging
import sys


def init_logger():
    # define logging path with the current time
    time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    log_path = "artifacts/logs/%s.log" % time

    # define log format
    logFormatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s")

    # define root logger
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.INFO)

    # add file handler to root logger
    fileHandler = logging.FileHandler(log_path)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    # add console handler to root logger
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)