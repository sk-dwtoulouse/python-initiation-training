from PySide6.QtGui import QIcon, QBrush, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QWidget, QMainWindow

if __name__ == "__main__":
    application = QApplication()
    # Load main window with list widget from Designer file
    window: QMainWindow = QUiLoader().load("files/list-widget.ui")
    list1: QListWidget = window.list1
    # Add icon
    sleep_icon = QIcon.fromTheme("text-x-python")
    for i in range(20):
        item = QListWidgetItem(sleep_icon, f"Élément {i}")
        list1.addItem(item)

    def on_clicked(list_item: QListWidgetItem):
        print(list_item.text())

    list1.itemClicked.connect(on_clicked)
    window.show()
    application.exec()
