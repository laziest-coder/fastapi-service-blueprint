import sys
from loguru import logger
import settings


def get_logger():
    logger.remove()
    logger.add(
                sys.stderr,
                format="{level} | {time} | {message} | context: {extra[context]}",
                colorize=True,
                level=settings.APP_DEBUG_LEVEL
               )
    return logger.bind(context={}) # giving default empty dict to context so as not to give it even when not needed
