# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginai.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from calender1_Beta import Ui_MainWindow

class Ui_Login_pg(object):
    def setupUi(self, Login_pg):
        Login_pg.setObjectName("Login_pg")
        Login_pg.resize(710, 552)
        self.centralwidget = QtWidgets.QWidget(Login_pg)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 600))
        self.label.setStyleSheet("background-color: rgb(56, 249, 251);\n""border-radius: 10px")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("picture6.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 100, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 270, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 210, 251, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(56, 249, 251);\n""border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(55)
        self.lineEdit.setFont(font)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 270, 251, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(56, 249, 251);\n""border-radius: 10px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        sfont = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(55)
        self.lineEdit_2.setFont(font)
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 0, 191, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Picture1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 370, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(56, 249, 251);\n""color: rgb(0, 0, 0);\n""border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.operationpg)
        Login_pg.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(Login_pg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 26))
        self.menubar.setObjectName("menubar")
        Login_pg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login_pg)
        self.statusbar.setObjectName("statusbar")
        Login_pg.setStatusBar(self.statusbar)

        self.retranslateUi(Login_pg)
        QtCore.QMetaObject.connectSlotsByName(Login_pg)
        
        
    def operationpg(self):
        msg = QMessageBox()
        if (self.lineEdit.text() == 'athrv01' and self.lineEdit_2.text() == 'innovations'):
            '''self.window2=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self.window2)
            Login_pg.hide()
            self.window2.showMaximized()'''
            import subprocess
            subprocess.Popen(['calender1_Beta.exe'],shell=True)
            Login_pg.close()
        else:
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Login Error")
            msg.setText('Incorrect details')
            msg.exec_()
            Login_pg.show()
        

    def retranslateUi(self, Login_pg):
        _translate = QtCore.QCoreApplication.translate
        Login_pg.setWindowTitle(_translate("Login_pg", "Login details"))
        self.label_2.setText(_translate("Login_pg", "User Login"))
        self.label_3.setText(_translate("Login_pg", "UserID"))
        self.label_4.setText(_translate("Login_pg", "Password"))
        self.pushButton.setText(_translate("Login_pg", "Sign- In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_pg = QtWidgets.QMainWindow()
    ui = Ui_Login_pg()
    ui.setupUi(Login_pg)
    Login_pg.show()
    sys.exit(app.exec_())
