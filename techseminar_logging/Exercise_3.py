import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# declare and attach your formatter here

# ---------

console_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(console_handler)

logger.info('Hello')