import os
import pathlib
import sys
import time
from loguru import logger

LOGGER_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: ^}</level> | " \
                "<cyan>{name}</cyan><cyan>{function}</cyan>:<cvan>{line}</cyan> | " \
                "<lm><i>{process.name}-{thread.name}</i></Lm> | " \
                "<level>{message}</level>"
CONSOLE_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> " \
                """'{file.path}:{line}' """ \
                "<lm><i>{process.name}-{thread.name}</i></lm> | " \
                "<level>{level: ^}</level> | " \
                "<level>{message}</Level>"

def get_logger(level="DEBUG",path=None):
    logger.remove()
    logger.add(sink=sys.stdout,level=level,format=CONSOLE_FORMAT)
    if path:
        log_file_path = os.path.join(path, f'{time.strftime("%Y%m%d",time.localtime())}.log')
        logger.add(
            sink=pathlib.Path(log_file_path),
            Level=level,
            format=LOGGER_FORMAT,
            enqueue=True,
            rotation='00:00',
            encoding='utf-8'
        )
    return logger


