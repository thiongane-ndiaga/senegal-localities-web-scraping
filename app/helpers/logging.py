import logging
import logging.handlers
import os

"""formatter = OneLineExceptionFormatter(
        "%(levelname)s - %(asctime)s - %(module)s - %(message)s")"""


def get_console_handler():
    # Set formats for each log handler
    ch_fmt = "%(asctime)s | %(levelname)s | %(module)s:%(lineno)d | %(message)s"
    ch_date_fmt = '%d-%b-%y %H:%M:%S'

    # create handler
    console_handler = logging.StreamHandler()

    # create formatter and add it to the handler
    ch_formatter = logging.Formatter(fmt=ch_fmt, datefmt=ch_date_fmt)
    console_handler.setFormatter(ch_formatter)

    # Set logging level
    console_handler.setLevel(logging.INFO)

    return console_handler


def get_logger() -> logging.Logger:
    # get handlers
    console_handler = get_console_handler()

    # create a logger with a log level and add the handlers to the logger
    logger = logging.getLogger()
    logger.setLevel(level=os.environ.get("LOGLEVEL", "INFO"))

    logger.addHandler(console_handler)

    return logger


logger = get_logger()
