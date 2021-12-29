import logging
import datetime


def init_logger():
    # define logging path with the current time
    time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    log_path = "artifacts/logs/{}.log" % time

    # define log format
    logFormatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s")

    # define root logger
    rootLogger = logging.getLogger()

    # add file handler to root logger
    fileHandler = logging.FileHandler(log_path)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    # add console handler to root logger
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)