import logging
from os.path import getsize


logger = logging.getLogger("data.basemanager")


class BaseManager:
    """Base data file manager."""

    def __init__(self, path: str):
        self._path = path
        logger.info(f"New file manager initialized for file {path}")

    def get_info(self) -> dict:
        """Get basic information about the file."""
        try:
            data = {"size": getsize(self._path)}
            return data
        except IOError:
            logger.error("Could not get file size.")
            return {"size": -1}


