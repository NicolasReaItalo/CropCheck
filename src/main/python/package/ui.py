# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(367, 293)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.btn_choose_file = QPushButton(self.centralwidget)
        self.btn_choose_file.setObjectName(u"btn_choose_file")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.btn_choose_file)

        self.lbl_file_name = QLabel(self.centralwidget)
        self.lbl_file_name.setObjectName(u"lbl_file_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lbl_file_name)

        self.lbl_up_offset = QLabel(self.centralwidget)
        self.lbl_up_offset.setObjectName(u"lbl_up_offset")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_up_offset)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.lbl_bottom_offset = QLabel(self.centralwidget)
        self.lbl_bottom_offset.setObjectName(u"lbl_bottom_offset")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_bottom_offset)

        self.lbl_left_offset = QLabel(self.centralwidget)
        self.lbl_left_offset.setObjectName(u"lbl_left_offset")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_left_offset)

        self.lbl_right_offset = QLabel(self.centralwidget)
        self.lbl_right_offset.setObjectName(u"lbl_right_offset")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_right_offset)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_5)

        self.lbl_satrt_tc = QLabel(self.centralwidget)
        self.lbl_satrt_tc.setObjectName(u"lbl_satrt_tc")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_satrt_tc)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit)

        self.lbl_resolution = QLabel(self.centralwidget)
        self.lbl_resolution.setObjectName(u"lbl_resolution")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_resolution)

        self.lbl_res_retrieve = QLabel(self.centralwidget)
        self.lbl_res_retrieve.setObjectName(u"lbl_res_retrieve")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lbl_res_retrieve)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_choose_file.setText(QCoreApplication.translate("MainWindow", u"Ouvrir ", None))
        self.lbl_file_name.setText(QCoreApplication.translate("MainWindow", u"nom du fichier", None))
        self.lbl_up_offset.setText(QCoreApplication.translate("MainWindow", u"Offset Haut", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_bottom_offset.setText(QCoreApplication.translate("MainWindow", u"Offset Bas", None))
        self.lbl_left_offset.setText(QCoreApplication.translate("MainWindow", u"Offset Gauche", None))
        self.lbl_right_offset.setText(QCoreApplication.translate("MainWindow", u"Offset Droite", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_satrt_tc.setText(QCoreApplication.translate("MainWindow", u"Commencer au TC", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"01:00:00:00", None))
        self.lbl_resolution.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.lbl_res_retrieve.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
    # retranslateUi

