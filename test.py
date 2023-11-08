import unittest
from unittest.mock import patch
from main import Ui_dialog
from PySide6 import QtCore, QtWidgets
import sys
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

    @patch('PyDub.AudioSegment.from_file')
    def test_file(self, mock_from_file):
        mock_audio = mock_from_file.return_value

        # simulated selected format
        self.ui.comboBox.setCurrentText('mp3')

        # simulate chosing bitrate
        self.ui.comboBox2.setCurrentText('128k')

        self.ui.file_name = "/path/to/file.wav"
        self.ui.directory = "path/to/directory"

        self.ui.convert()

        # Assertions
        mock_audio.export.assert_called_once_with(
            '/path/to/your/directory/file.mp3', format='mp3', bitrate='128k'
        )

