import csv
import logging

from data.basemanager import BaseManager


logger = logging.getLogger("data.csvmanager")


class CSVManager(BaseManager):
    """Data manager for CSV files."""

    def get_info(self) -> dict:
        data = super().get_info()
        try:
            with open(self._path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for idx, _ in enumerate(reader):
                    pass
                data["rows"] = idx
            return data
        except IOError:
            logger.error("Could not decode CSV, IO error occurred.")
            return data
        except UnicodeDecodeError:
            logger.error("CSV is not encoded in UTF8, skipping.")
            return data

