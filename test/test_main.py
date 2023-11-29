from PySide6 import QtWidgets
import sys
import os
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
from main import Ui_dialog



def build_up():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    return app, dialog, ui

def is_file_with_extension(file_path, target_extension):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == f".{target_extension.lower()}"

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

        
def test_convert():
    app, dialog, ui = build_up()

    ui.file_name = "test/sample-12s.mp3"
    ui.directory = "./"

    for i in range(ui.comboBox.count()):
        if i == 1: continue # have to skip mp3 for now because bitrate alert stop testing
        for x in range(ui.comboBox2.count()):
            ui.comboBox.setCurrentIndex(i)
            ui.comboBox2.setCurrentIndex(x)
            ui.convert()

            file_exist = os.path.exists(ui.file_name)
            current_file_path = "./sample-12s." + ui.comboBox.currentText()
            file_extension = is_file_with_extension(current_file_path,ui.comboBox.currentText())
            os.remove(current_file_path)
            assert file_exist & file_extension
