from data.csvmanager import CSVManager
from data.basemanager import BaseManager


if __name__ == '__main__':
    csv1 = CSVManager("files/demo-csv.csv")
    csv2 = CSVManager("files/demo-csv-incorrect.csv")
    base1 = BaseManager("files/demo-csv.csv")
    print(csv1.get_info())
    print(csv2.get_info())
