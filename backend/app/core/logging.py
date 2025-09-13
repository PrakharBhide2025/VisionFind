import logging, sys
from loguru import logger

class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except Exception:
            level = record.levelno
        logger.bind(module=record.module).opt(depth=6, exception=record.exc_info).log(
            level, record.getMessage()
        )

def configure_logging():
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
    logger.remove()
    logger.add(sys.stdout, level="INFO", enqueue=True, backtrace=False, diagnose=False)
