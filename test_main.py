from PySide6 import QtWidgets
from main import Ui_dialog
import sys

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

def test_comobox():
    app, dialog, ui = build_up()
    type_list = ["wav","mp3","flac","ogg","m4a","aiff"]

    for i in range(ui.comboBox.count()):
        assert ui.comboBox.itemText(i) == type_list[i]

    type_list_2 = ["32k","64k","128k","256k","320k"]
    
    for i in range(ui.comboBox2.count()):
        assert ui.comboBox2.itemText(i) == type_list_2[i]

        
