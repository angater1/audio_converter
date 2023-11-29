from PySide6 import QtWidgets
from PySide6.QtTest import QTest
from unittest.mock import patch
from main import Ui_dialog
import pytest
# from pytestqt.qtbot import QtBot
import sys
import pytestqt

@pytest.fixture
def qtbot(qtbot):
    """Pytest fixture for QtBot."""
    return qtbot

def build_up():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    return app, dialog, ui

def test_pushbutton_text():
    app, dialog, ui = build_up()

    assert ui.pushButton.text() == "Choose audio file"
    assert ui.pushButton_2.text() == "Choose your destination"
    assert ui.pushButton_3.text() == "Convert"

def test_label():
    app, dialog, ui = build_up()

    assert ui.file_name == ""
    assert ui.directory == ""
