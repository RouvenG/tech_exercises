import logging
import sys

logger = logging.getLogger()


console_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(console_handler)

logger.info('Hello')