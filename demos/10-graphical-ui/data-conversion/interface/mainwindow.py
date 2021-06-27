from PySide6.QtWidgets import QMainWindow, QPushButton, QListWidget


class MainWindow(QMainWindow):
    """
    Class written just for autocompletion and type hinting.

    Lists dynamic attributes of the loaded window
    so that PyCharm can know that the following attributes
    exist in the loaded file.

    The class is then used for type hinting in the
    `WindowManager` class.

    """
    file_button: QPushButton
    button_csv_export: QPushButton
    button_txt_export: QPushButton
    list_widget: QListWidget
