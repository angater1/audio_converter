import unittest
from unittest.mock import patch
from PyQt5.QtTest import QTest
import sys
sys.path.append('../audio_converter')
from main import Ui_dialog
from PySide6 import QtCore, QtWidgets
from pydub import AudioSegment

class TestUiDialog(unittest.TestCase):

    def setUp(self):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()
        self.dialog = QtWidgets.QDialog()  
        self.ui = Ui_dialog()
        self.ui.setupUi(self.dialog)  

    def test_initialization(self):
        # check if variable is empty
        self.assertEqual(self.ui.file_name, " ")
        self.assertEqual(self.ui.directory, " ")
        self.assertEqual(self.ui.progressbar, 0)

    # @patch('pydub.AudioSegment.from_file')
    # def test_convert_button(self, mock_audio_from_file):
    #     # Symulowanie wyboru opcji w Twojej aplikacji
    #     self.ui.comboBox.setCurrentIndex(1)  # Wybierz format mp3
    #     self.ui.comboBox2.setCurrentIndex(2)  # Wybierz bitrate 128k

    #     # Symulacja naciśnięcia przycisku konwersji
    #     QTest.mouseClick(self.ui.pushButton_3, Qt.LeftButton)

    #     # Poczekaj, aż okno lub dialog się pojawi
    #     QTest.qWaitForWindowExposed(self.dialog)

    #     # Sprawdź oczekiwane wyniki lub zachowanie
    #     self.assertTrue(self.ui.progressBar.isVisible())
    #     self.assertTrue(self.ui.completed > 0)


unittest.main()