import logging
import sys

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
