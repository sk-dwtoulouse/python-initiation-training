import logging
import sys

logger = logging.getLogger("data")

# Configure the main logger for the data package
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    formatting = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatting)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.debug("Data logger registered.")
