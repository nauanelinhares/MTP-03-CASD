# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlbertoUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from time import sleep
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import funcoesBot

"""
Antes de rodar o código:
1. instale as seguintes bibliotecas:
    - Selenium
    - time
    - PyQt6
    - PyQt5
    - gspread
    Para instalar a biblioteca basta escreve no promt de comando:
        pip install "biblioteca"
2. Tenha o google chrome e instalado
3. Baixe o chromedriver para utilizar o selenium: 
    https://chromedriver.chromium.org/downloads

"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 785)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(80, 480, 171, 101))
        self.frame_2.setMaximumSize(QtCore.QSize(300, 160))
        self.frame_2.setStyleSheet("background-color: rgb(249, 179, 66);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lobster 1.4\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-10, 0, 61, 961))
        self.frame_3.setStyleSheet("background-color: rgb(112, 111, 111);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(80, 600, 171, 101))
        self.frame_4.setMaximumSize(QtCore.QSize(300, 160))
        self.frame_4.setStyleSheet("background-color: rgb(49, 146, 179);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lobster 1.4\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 50, 521, 401))
        self.frame.setStyleSheet("\n"
"image: url(Alberto Ok.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 540, 461, 31))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("\n"
"font: 12pt \"Lobster 1.4\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 661, 51))
        self.label.setStyleSheet("font: 16pt \"Lobster 1.4\" ;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 470, 461, 51))
        self.label_2.setStyleSheet("font: 15pt \"Lobster 1.4\" ;\n"
"qproperty-alignment: AlignCenter;\n"
"border: 1px solid rgb(49, 146, 179)")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlbertoBot"))
        MainWindow.setWindowIcon(QIcon('alberto.ico'))
        self.pushButton.setText(_translate("MainWindow", "Iniciar"))
        self.pushButton_2.setText(_translate("MainWindow", "Finalizar"))
        self.pushButton_3.setText(_translate("MainWindow", "Enviar Mensagens"))
        self.label.setText(_translate("MainWindow", "Olá, eu sou o Alberto Bot, selecione o que você deseja fazer 😃:"))
        self.label_2.setText(_translate("MainWindow", "Funções"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
