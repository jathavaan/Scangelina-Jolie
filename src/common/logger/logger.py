import logging
import ntpath
import os

from .ilogger import ILogger
from ... import Config


class Logger(ILogger):
    __logger: logging.Logger

    def __init__(self) -> None:
        filename: str = ntpath.basename(__file__).replace(".py", ".log")
        file_path: str = os.path.join(Config.LOG_DIR.value, filename)

        logging.basicConfig(level=Config.LOGGING_LEVEL.value)
        logger = logging.getLogger(__name__)

        handler = logging.FileHandler(filename=file_path, mode="a")
        formatter = logging.Formatter(
            fmt='{:<15}{:<15}{:<15}{:<15}'.format('%(asctime)s', '%(levelname)s', '%(filename)s', '%(message)s'),
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.logger = logger

    @property
    def logger(self) -> logging.Logger:
        return self.__logger

    @logger.setter
    def logger(self, logger: logging.Logger) -> None:
        self.__logger = logger

    def debug(self, message) -> None:
        self.logger.debug(message)

    def info(self, message) -> None:
        self.logger.info(message)

    def warning(self, message) -> None:
        self.logger.warning(message)

    def error(self, message) -> None:
        self.logger.error(message)

    def critical(self, message) -> None:
        self.logger.critical(message)
