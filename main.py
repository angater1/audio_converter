from tkinter.filedialog import *
from PySide6.QtGui import QFont
from pydub import AudioSegment
from PySide6 import QtCore, QtWidgets
import eyed3

class Ui_dialog(object):

    def setupUi(self, dialog, file_name="", directory=""):
        dialog.setObjectName("dialog")
        dialog.resize(391, 287)

        self.progressbar = 0
        self.file_name = file_name
        self.directory = directory
        self.name = ""

        #ok, cancel
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 250, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")

        #choose file
        self.pushButton = QtWidgets.QPushButton(dialog, clicked=lambda: self.file())
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 161, 41))
        self.pushButton.setObjectName("chooseFile")

        #choose destination
        self.pushButton_2 = QtWidgets.QPushButton(dialog, clicked=lambda: self.destination())
        self.pushButton_2.setGeometry(QtCore.QRect(220, 10, 161, 41))
        self.pushButton_2.setObjectName("chooseDestination")

        #convert button
        self.pushButton_3 = QtWidgets.QPushButton(dialog, clicked=lambda: self.convert())
        self.pushButton_3.setGeometry(QtCore.QRect(10, 250, 100, 32))
        self.pushButton_3.setObjectName("chooseFile")

        #choose format
        self.comboBox = QtWidgets.QComboBox(dialog)
        self.comboBox.setGeometry(QtCore.QRect(260, 110, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.on_combobox_changed)

        #choose bitrate for mp3
        self.comboBox2 = QtWidgets.QComboBox(dialog)
        self.comboBox2.setGeometry(QtCore.QRect(260, 150, 69, 22))
        self.comboBox2.setObjectName("comboBox")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.setVisible(False)

        # progressbar
        self.progressBar = QtWidgets.QProgressBar(dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 210, 371, 23))
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)

        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(250, 80, 91, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        #input file
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 91, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        #filename
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 112, 100, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")

        #arrow
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 47, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        #destination label:
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 91, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        #choose output info
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(100, 200, 220, 50))
        self.label_7.setAlignment(QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(QFont('Arial', 15))
        self.label_7.setVisible(False)

        #output text edit
        self.text_edit = QtWidgets.QLineEdit(dialog)
        self.text_edit.setPlaceholderText("destination path")
        self.text_edit.setGeometry(20, 160, 200, 21)

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dialog)

    #function that asks for input file
    def file(self):
        self.file_name = askopenfilename()
        # print(self.file_name.split("/"))
        self.input_file = self.file_name.split("/")
        self.name = str(self.input_file[-1])
        self.retranslateUi(dialog)

    #function that asks for output directory
    def destination(self):
        self.directory = askdirectory()
        if self.directory != "":
            self.directory += "/"
        self.retranslateUi(dialog)

    #function that does the conversion
    def convert(self):
        # filename without extension
        input_file = self.file_name.split("/")
        name = str(input_file[-1])
        for r in ((".mp3", ""), (".wav", ""), (".flac", ""), (".ogg", ""), (".m4a", ""), (".aiff", "")): #delete file extension
            name = name.replace(*r)
        
        chosen_format = str(self.comboBox.currentText())
        bitrate = str(self.comboBox2.currentText())

        name = self.text_edit.text() + "/" + name
        print(self.text_edit.text() + "/" + name)

        try:
            self.label_7.setVisible(False)
            if chosen_format == "mp3":

                # comapre input and output bitrate
                audiofile = eyed3.load(self.file_name)
                input_bitrate = audiofile.info.bit_rate_str
                input_bitrate = int(input_bitrate.rstrip(' kb/s'))

                # show allert if input bitrate is less than output bitrate
                if (input_bitrate < int(bitrate.rstrip('k'))):
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setWindowTitle("Bitrate Alert")
                    msg.setText(f"The current bitrate is {bitrate}bps, which is higher than the original file (e.g., {input_bitrate} kbps)." 
                                "A higher bitrate can lead to audio distortions, loss of quality, or inconsistencies with the original recording."
                                "To avoid undesirable effects, consider adjusting the conversion settings or selecting a lower bitrate.")
                    # buttons
                    continue_button = msg.addButton("Continue", QtWidgets.QMessageBox.AcceptRole)
                    cancel_button = msg.addButton("Cancel", QtWidgets.QMessageBox.RejectRole)
                    msg.exec()

                    if msg.clickedButton() == cancel_button:
                        return

                AudioSegment.from_file(self.file_name).export(self.text_edit.text(),
                                                              bitrate = bitrate, format=chosen_format)
                self.progressBar.setVisible(True)
                self.completed = 0
                while self.completed < 100:
                    self.completed += 0.0001
                    self.progressBar.setValue(self.completed)
            else:
                AudioSegment.from_file(self.file_name).export(self.text_edit.text(),
                                                              format=chosen_format)
                self.progressBar.setVisible(True)
                self.completed = 0
                while self.completed < 100:
                    self.completed += 0.0001
                    self.progressBar.setValue(self.completed)
        except Exception as error:
            self.label_7.setVisible(True)
            print(error)

    #refresh ui on combobox change
    def on_combobox_changed(self):
        if self.name != "":
            for r in ((".mp3", ""), (".wav", ""), (".flac", ""), (".ogg", ""), (".m4a", ""), (".aiff", "")): #delete file extension
                self.name = self.name.replace(*r)
            self.name = self.name + "." + self.comboBox.currentText()
        if self.comboBox.currentText() == 'mp3':
            self.comboBox2.setVisible(True)
        else:
            self.comboBox2.setVisible(False)
        self.retranslateUi(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.pushButton.setText(_translate("dialog", "Choose audio file"))
        self.pushButton_2.setText(_translate("dialog", "Choose your destination"))
        self.pushButton_3.setText(_translate("dialog", "Convert"))
        self.comboBox.setItemText(0, _translate("dialog", "wav"))
        self.comboBox.setItemText(1, _translate("dialog", "mp3"))
        self.comboBox.setItemText(2, _translate("dialog", "flac"))
        self.comboBox.setItemText(3, _translate("dialog", "ogg"))
        self.comboBox.setItemText(4, _translate("dialog", "m4a"))
        self.comboBox.setItemText(5, _translate("dialog", "aiff"))
        self.label.setText(_translate("dialog", "Convert to:"))
        self.label_2.setText(_translate("dialog", "Your file:"))
        self.label_3.setText(_translate("dialog", self.file_name.split("/")[-1]))
        self.label_4.setText(_translate("dialog", "-------->"))
        self.label_6.setText(_translate("dialog", "Destination:"))
        self.label_7.setText(_translate("dialog", "CHOOSE OUTPUT!"))
        self.comboBox2.setItemText(0, _translate("dialog", "32k"))
        self.comboBox2.setItemText(1, _translate("dialog", "64k"))
        self.comboBox2.setItemText(2, _translate("dialog", "128k"))
        self.comboBox2.setItemText(3, _translate("dialog", "256k"))
        self.comboBox2.setItemText(4, _translate("dialog", "320k"))

        #set text in destination text edit
        dest_text = self.text_edit.text()
        if dest_text == "":
            self.text_edit.setText(_translate("dialog", self.directory + self.name))
        else:
            self.text_edit.setText(_translate("dialog", self.directory + self.name))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec())
