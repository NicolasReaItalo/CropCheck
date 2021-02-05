from PySide2.QtWidgets import QMainWindow
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets

import sys

from package import timecode, video_utils
from package.ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.show()


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Window()

   # window.show()
   # path = str(QtWidgets.QFileDialog.getOpenFileName()[0])

    #video_utils.play_video(path)

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)