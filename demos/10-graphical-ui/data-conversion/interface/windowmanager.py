from typing import Union

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QFileDialog, QWidget, QListWidgetItem

from interface.mainwindow import MainWindow
from loaders import CSVManager


class WindowManager:
    """
    Class used to manage the Qt window and its associated data.

    Attributes:
        _window: Private, contains the main window.
        _csv_manager: Private, holds a CSV manager.

    """
    _window: Union[QWidget, MainWindow] = None  # Qt window managed by this class
    _csv_manager: CSVManager = None  # Object used to manage CSV data

    def __init__(self):
        """
        Initialize our window manager.

        """
        loader = QUiLoader()
        self._window = loader.load("files/designer/demo-dialog.ui")
        # Once the window is loaded, connect actions to code
        self.setup_actions()

    def setup_actions(self):
        """Connect actions of controls to methods."""
        self._window.file_button.clicked.connect(self.on_file_select)
        self._window.button_csv_export.clicked.connect(self.on_export_csv)

    def on_file_select(self):
        """
        Action when the file button is clicked.

        Shows a file select dialog to pick a CSV
        and loads the CSV file in the CSVManager instance of the object.

        """
        filter_text = "CSV File (*.csv)"
        selection: tuple = QFileDialog.getOpenFileName(self._window, "CSV File", "", filter_text)
        path: str = selection[0]
        if path:
            self._csv_manager = CSVManager(path)
            self._window.button_csv_export.setEnabled(True)
            # Empty and enable the list widget
            self._window.list_widget.clear()
            self._window.list_widget.setEnabled(True)
            for row in self._csv_manager.data:
                item = QListWidgetItem(";".join(row))
                self._window.list_widget.addItem(item)

    def on_export_csv(self):
        """
        Action when the export to CSV button is clicked.

        Shows a file select dialog to select a file destination.
        The output file is then saved to the selected path.

        """
        filter_text = "Text File (*.txt)"
        selection: tuple = QFileDialog.getSaveFileName(self._window, "Text File", "", filter_text)
        path: str = selection[0]
        if path:
            self._csv_manager.export_text(selection[0])

    def show(self):
        """
        Public method to show our window.

        The window is loaded automatically at instanciation
        in the `__init__` method.

        """
        self._window.show()
