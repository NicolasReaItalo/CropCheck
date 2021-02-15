from PySide2.QtWidgets import QMainWindow
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets

import os
import sys

from package import timecode, video_utils
from package.ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Crop Check")
        # Global variables
        self.file_path = ''
        self.res_x = 0
        self.res_y = 0
        self.offset_top =0
        self.offset_bottom =0
        self.offset_right =0
        self.offset_left =0

        # Connexions
        self.btn_choose_file.clicked.connect(self.press_file_button)
        self.pushButton_2.clicked.connect(self.press_analyse_button)


        self.show()

    def press_file_button(self):
        self.file_path = str(QtWidgets.QFileDialog.getOpenFileName()[0])
        self.lbl_file_name.setText(os.path.basename(self.file_path))
        self.res_x, self.res_y = video_utils.get_resolution(self.file_path)
        self.lbl_res_retrieve.setText(f'{self.res_x}x{self.res_y}')
        self.lbl_file_name.repaint()
        self.lbl_resolution.repaint()

    def press_analyse_button(self):
        if self.file_path != '':
            video_utils.analyse_video_pass_01(self.file_path,0,0,self.offset_top,self.offset_bottom,self.offset_left,
                                              self.offset_right)





if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Window()



    #video_utils.play_video(path)

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)