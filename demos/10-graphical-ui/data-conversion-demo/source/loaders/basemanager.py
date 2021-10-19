from abc import ABC, abstractmethod
from loaders.formats import DataFormat


class BaseDataManager(ABC):
    """Base class for data managers."""

    @abstractmethod
    def load(self, url: str, encoding: str = "iso8859-1"):
        """Load data for the manager."""
        pass

    @abstractmethod
    def export(self, url: str, fmt: DataFormat):
        """Export data in a specific format."""
        pass
