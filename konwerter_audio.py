# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'konwerter_audio.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import ffmpeg
import AudioConverter
from tkinter.filedialog import *

from PySide6 import QtCore, QtWidgets, QtGui

progressbar = 0

class Ui_dialog(object):

    def setupUi(self, dialog, file_name = " ", directory = " "):
        dialog.setObjectName("dialog")
        dialog.resize(391, 287)
       

        self.file_name = file_name
        self.directory = directory

        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 250, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        #choose file
        self.pushButton = QtWidgets.QPushButton(dialog, clicked=lambda: self.file())
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 161, 41))
        self.pushButton.setObjectName("chooseFile")

        #choose destination
        self.pushButton_2 = QtWidgets.QPushButton(dialog, clicked=lambda: self.destination())
        self.pushButton_2.setGeometry(QtCore.QRect(10, 240, 161, 41))
        self.pushButton_2.setObjectName("chooseDestination")

        self.comboBox = QtWidgets.QComboBox(dialog)
        self.comboBox.setGeometry(QtCore.QRect(260, 110, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        #progressbar
        self.progressBar = QtWidgets.QProgressBar(dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 210, 371, 23))
        self.progressBar.setProperty("value", progressbar)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)

        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(250, 80, 91, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        #yourfile
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 91, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        #filename
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 112, 100, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 47, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 132, 300, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 91, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")


        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def file(self):
        self.file_name = askopenfilename()
        #print(self.file_name.split("/"))
        self.retranslateUi(dialog)
        
    def destination(self):
        self.directory = askdirectory()
        #print(self.file_name.split("/"))
        self.retranslateUi(dialog)


    def retranslateUi(self, dialog):


        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.pushButton.setText(_translate("dialog", "Choose audio file"))
        self.pushButton_2.setText(_translate("dialog", "Choose your destination"))
        self.comboBox.setItemText(0, _translate("dialog", "MP3"))
        self.comboBox.setItemText(1, _translate("dialog", "WAV"))
        self.comboBox.setItemText(2, _translate("dialog", "FLAC"))
        self.comboBox.setItemText(3, _translate("dialog", "OGG"))
        self.comboBox.setItemText(4, _translate("dialog", "M4A"))
        self.comboBox.setItemText(5, _translate("dialog", "AIFF"))
        self.label.setText(_translate("dialog", "Convert to:"))
        self.label_2.setText(_translate("dialog", "Your file:"))
        self.label_3.setText(_translate("dialog", self.file_name.split("/")[-1]))
        self.label_4.setText(_translate("dialog", "-------->"))
        self.label_5.setText(_translate("dialog", self.directory))
        self.label_6.setText(_translate("dialog", "Destination:"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
