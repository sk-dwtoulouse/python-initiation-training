import csv


class CSVManager:
    """
    Utility class to keep CSV data for export in other formats.

    Attributes:
        data: Contains loaded file data as a list of lists.

    """

    data: list = None

    def __init__(self, url: str):
        """
        Initialize the object with a URL.

        Args:
            url: CSV URL to load from.

        """
        self.load(url)

    def load(self, url: str, encoding: str = "iso8859-1"):
        """
        Load a CSV given its file path.

        Args:
            url: Path of the CSV file.
            encoding: Codepage name of the text file.

        """
        with open(url, "r", encoding=encoding) as f:
            reader = csv.reader(f, delimiter=",")
            if self.data is None:
                self.data = []
            for row in reader:
                self.data.append(row)

    def export_text(self, url: str):
        """
        Save data as a text file.

        Every column is save in its own line as an example.

        Args:
            url: Output file path.

        """
        with open(url, "w", encoding="utf-8") as file:
            for row in self.data:
                file.write("\n".join(row))

    def export_csv(self, url: str):
        """
        Save data as a CSV file with semicolons.

        Args:
            url: Output file path.

        """
        with open(url, "w", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            for row in self.data:
                writer.writerow(row)
