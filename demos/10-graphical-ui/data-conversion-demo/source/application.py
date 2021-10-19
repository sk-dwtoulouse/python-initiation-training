"""
Entry point for our demo application.

Uses a "WindowManager" class holding the main window and the
CSV data manager used in it.

.. include:: documentation/includes/application.md

"""
from PySide6.QtWidgets import QApplication

from interface import WindowManager  # look at interface/__init__.py

if __name__ == "__main__":
    print(__module__)
    application = QApplication()
    window_manager = WindowManager()
    window_manager.show()
    application.exec()
