import sys

from loguru import logger


class CustomLogger:
    def __init__(self):
        self.logger_custom = logger
        self.logger_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "  # Time format
            "<level>{level: <8}</level> | "  # Log level format
            "<cyan>{name}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> | "  # Module.function:line format
            "<level>{message}</level>"  # Log message format
        )

        self.logger_custom.remove()  # Removing any existing log handlers
        self.logger_custom.add(
            sys.stderr, format=self.logger_format, backtrace=True, diagnose=True, enqueue=True, context=None, catch=True
        )  # Adding a log handler to output to standard error


logger_config = CustomLogger()

log = logger_config.logger_custom
