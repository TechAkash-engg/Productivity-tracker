# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calender2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys,os
from datetime import datetime, timedelta
from dateutil.relativedelta import *
import calendar
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget , QCalendarWidget, QLabel, QComboBox, QMessageBox
from PyQt5.QtCore import QDate
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    global currentYear, currentMonth, currentDay
    global js
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    currentDay = datetime.now().day
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1882, 851)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1930, 1000))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("picture13.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1450, 520, 397, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(2, 61, 148);\n""border-radius: 20px;")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated.connect(self.selectionchange)
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1400, 945, 511, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(950, 710, 420, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(60, 160, 821, 780))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(550)
        self.calendar.setFont(font)
        self.calendar.setStyleSheet("font: 75 10pt \"Arial\";\n""color: rgb(0, 0, 0);\n""background-color: rgb(0, 161, 255);\n""")
        self.calendar.setMinimumDate(QtCore.QDate(1847, 9, 14))
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendar.setGridVisible(True)
        self.calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setObjectName("calendar")
        self.calendar.setMinimumDate(QDate(currentYear, currentMonth - 8,currentDay))
        self.calendar.setMaximumDate(QDate(currentYear, currentMonth + 8, calendar.monthrange(currentYear, currentMonth)[1]))
        self.calendar.setSelectedDate(QDate(currentYear, currentMonth, currentDay))
        self.calendar.clicked.connect(self.printDateInfo)
        
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(1730, 0, 280, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet("background-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.lbl.setText("")
        self.lbl.setObjectName("lbl")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 0, 781, 151))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Picture1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(950, 290, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(2, 61, 148);\n""border-radius: 20px;")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.activated.connect(self.selectionweek)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1450, 270, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_3.setAcceptDrops(True)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(2, 61, 148);\n""border-radius :20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.select_month)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(950, 480, 450, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1450, 480, 450, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(950, 250, 350, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(2, 61, 148);\n""border-radius :10px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.weekly_all)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1450, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(2, 61, 148);\n""border-radius :10px;")
        self.pushButton_5.setObjectName("pushButton_6")
        self.pushButton_5.clicked.connect(self.monthly_all)
        
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(950, 520, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(2, 61, 148);\n""border-radius: 20px;")
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setMaxVisibleItems(10)
        self.comboBox_4.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_4.setDuplicatesEnabled(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.activated.connect(self.weekmail)
        
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(950, 750, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(2, 61, 148);\n""border-radius: 20px;")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setMaxVisibleItems(10)
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_3.setDuplicatesEnabled(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.activated.connect(self.viewpdf)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1882, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_4.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def printDateInfo(self, qDate):
        #print('{0}/{1}/{2}'.format( qDate.day(),qDate.month(), qDate.year()))
        self.lbl.setText(qDate.toString())

    #to generate monthly pdf     
    def select_month(self):
        import subprocess
        import time
        subprocess.Popen(['piemon1.py'],shell=True)
        #time.sleep(25)
        msg1 = QtWidgets.QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setText("Monthly Report has started to Generate.Wait for 30secs to complete this action")
        msg1.setWindowTitle("Message")
        msg1.exec_()
        
    #to mail weekly report to all   
    def weekly_all(self):
        import subprocess
        import time
        subprocess.Popen(['weekmail_all.py'],shell=True)
        time.sleep(15)
        msg2 = QtWidgets.QMessageBox()
        msg2.setIcon(QMessageBox.Information)
        msg2.setText("weekly report has been Mailed")
        msg2.setWindowTitle("Message")
        msg2.exec_()
        
    #to mail monthly report to all
    def monthly_all(self):
        import subprocess
        import time
        subprocess.Popen(['mailall.py'],shell=True)
        #time.sleep(15)
        msg3 = QtWidgets.QMessageBox()
        msg3.setIcon(QMessageBox.Information)
        msg3.setText("Monthly Report has been started to Mail. Wait for 30secs to complete this action")
        msg3.setWindowTitle("Message")
        msg3.exec_()
    
    #to mail the monthly pdf generated to individual    
    def selectionchange(self):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        i=self.comboBox.currentIndex() 
            
        if i==0:
            email_send = "akashrajpbhat@gmail.com"  
            filename ='Akashraj Bhat.pdf'
        elif i==1:
            email_send = "anarghyasr2000@gmail.com"       
            filename ='Anarghya S R.pdf'            
        elif i==2:
            email_send = "anush.laila.22@gmail.com"  
            filename ='Anush Laila.pdf'            
        elif i==3:
            email_send = "pranathiacharya1@gmail.com"        
            filename ='Pranathi Acharya.pdf'            
        elif i==4:
            email_send = "prathiknayak03@gmail.com"
            filename ='Prathik Nayak.pdf'            
        elif i==5:   
            email_send = "Vanshikashenoy07@gmail.com"
            filename ='Vanshika Shenoy.pdf'            
        elif i==6:
            email_send = "vikaspoojary110@gmail.com"
            filename ='Vikas.pdf'
        elif i==7:            
            email_send = "Abhishekdileep99@gmail.com"
            filename ='Abhishek Dileep.pdf'
        elif i==8:            
            email_send = "akshatharao532@gmail.com" 
            filename ='Akshatha.pdf'
        elif i==9:            
            email_send = "amansrivastav715@gmail.com"  
            filename ='Aman Kumar Srivastav.pdf'
        elif i==10:           
            email_send = "anjalipmadhyastha@gmail.com"  
            filename ='Anjali.pdf'
        elif i==11:        
            email_send = "ankithbhandary8@gmail.com"  
            filename ='Ankith Bhandary.pdf'
        elif i==12:            
            email_send = "arvikonoha@gmail.com"  
            filename ='Aravind B R.pdf'
        elif i==13:           
            email_send = "avishvshetty@gmail.com"  
            filename ='Avish Shetty.pdf'
        elif i==14:           
            email_send = "basanagoudap9141@gmail.com"  
            filename ='Basangouda Patil.pdf'
        elif i==15:            
            email_send = "Deekshithprabhu284@gmail.com"  
            filename ='Deekshith Prabhu.pdf'
        elif i==16:            
            email_send = "harshithagsuresh97@gmail.com"  
            filename ='Harshitha G S .pdf'
        elif i==17:            
            email_send = "josvincorda@gmail.com"
            filename ='Josvin.pdf'
        elif i==18:           
            email_send = "puranik.keerthana@gmail.com"  
            filename ='Keerthana.pdf'
        elif i==19:            
            email_send = "leeladharabhijeeth21@yahoo.com"  
            filename ='Leeladhar Shetty.pdf'
        elif i==20:            
            email_send = "Shettymeghana32@gmail.com"  
            filename ='Meghana.pdf'
        elif i==21:            
            email_send = "smokshithpergade@gmail.com"  
            filename ='Mokshith S Pergade.pdf'
        elif i==22:            
            email_send = "namyashetty2001@gmail.com"  
            filename ='Namya Shetty.pdf'
        elif i==23:            
            email_send = "nehauday2000@gmail.com" 
            filename ='Neha U.pdf'
        elif i==24:            
            email_send = "nidishnrao@gmail.com"  
            filename ='Nidish Rao.pdf'
        elif i==25:           
            email_send = "poornimadakshay26@gmail.com"  
            filename ='Poornima.pdf'
        elif i==26:            
            email_send = "pramodshet109@gmail.com"  
            filename ='Pramod Shet.pdf'
        elif i==27:            
            email_send = "hegdeprasidh6@gmail.com"  
            filename ='Prasidda Hegde.pdf'
        elif i==28:            
            email_send = "Prathikshau0987@gmail.com"  
            filename ='Prathiksha.pdf'
        elif i==29:            
            email_send = "praveensnayak12@gmail.com"
            filename ='Praveen Nayak.pdf'
        elif i==30:           
            email_send = "shettigarpreetham15@gmail.com"  
            filename ='Preetham G S.pdf'
        elif i==31:           
            email_send = "ranjitha.as.1998@gmail.com"  
            filename ='Ranjitha A S.pdf'
        elif i==32:           
            email_send = "rishabhgujarati@gmail.com" 
            filename ='Rishabh Gujarati.pdf'
        elif i==33:           
            email_send = "srudith14@gmail.com"  
            filename ='S R Udith.pdf'
        elif i==34:           
            email_send = "sameergp01@gmail.com"  
            filename ='Sameer G.pdf'
        elif i==35:            
            email_send = "sharathhulekal@gmail.com"  
            filename ='Sharath Hulekal.pdf'
        elif i==36:            
            email_send = "shashankhs333@gmail.com"
            filename ='Shashank H S.pdf'
        elif i==37:            
            email_send = "shreyar490@gmail.com"  
            filename ='Shreya R.pdf'
        elif i==38:            
            email_send = "shreyasmnglr9@gmail.com"  
            filename ='Shreyas S.pdf'
        elif i==39:            
            email_send = "kamathanand100@gmail.com"
            filename ='Shrinivas Anand Kamath.pdf'
        elif i==40:            
            email_send = "shubhamparmar262@gmail.com"  
            filename ='Shubham.pdf'
        elif i==41:            
            email_send = "sudhanva.udupi55@gmail.com"  
            filename ='Sudhanva Acharya.pdf'
        elif i==42:            
            email_send = "sushmitashetty2017@gmail.com"  
            filename ='Sushmita Shetty.pdf'
        elif i==43:            
            email_send = "bvadirajatantry413@gmail.com"  
            filename ='Vadiraj.pdf'
        elif i==44:            
            email_send = "varshagundoomane@gmail.com"  
            filename ='Varsha  G D.pdf'
        elif i==45:           
            email_send = "vidhinpatel7@gmail.com" 
            filename ='Vidhin.pdf'
        elif i==46:            
            email_send = "vigneshkini2000@gmail.com"
            filename ='Vignesh Kini.pdf'
        elif i==47:            
            email_send = "vijethap803@gmail.com" 
            filename ='Vijetha.pdf'
        elif i==48: 
            email_send = "Vineethshetty289@gmail.com"  
            filename ='Vineeth D Shetty.pdf'
        elif i==49:            
            email_send = "vru27091973@gmail.com"  
            filename ='Vrujesh H M.pdf'
        elif i==50:            
            email_send = "yogithasnaik123@gmail.com"
            filename ='Yogitha.pdf'
        elif i==51:            
            email_send = "dhanrajdeeru@gmail.com"
            filename ='Dhanraj.pdf'
        
            
                       
        email_user = 'Athrvservices@gmail.com'    #fromm mail id
        email_password = 'april@2020'                   #from: mail password        
        subject = 'Performance Report'
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        
        body = ("""Greetings of the day,

        Your monthly performance report is hereby attached along with this email.
        Review it for self evaluation, and Improve your performance.

        Report generated by Artificial Intelligence Team

        Have a great day!""")
        msg.attach(MIMEText(body,'plain'))
        attachment = open(filename, "rb")
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)
        server.sendmail(email_user,email_send,text)
        server.quit()
        
    #to get weeks report    
    def selectionweek(self):
        js=self.comboBox_2.currentIndex()
        #d=os.system('combine2.py')
        #print (d)
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        import datetime as dt
        from PyPDF2 import PdfFileMerger
        import time
        num=js
        for i in range(4):
            if i==0:
                name='anush'
            elif i==1:
                name='prathik'
            elif i==2:
                name='vanshika'
            elif i==3:
                name='vikas'
        
            df=pd.read_excel("E:\\AtharvED\\AI\\monweek_ex.xlsx",name)
            def array_creater(X):
                conv_list=[]
                for i in range(len(X)):
                    #j=df['Total'][i].strftime("%H:%M:%S")
                    j=X[i].strftime("%H:%M:%S")
                    conv_list.append(j)
                return conv_list
            a=df['Total']
            b=df['Learning']
            c=df['R&D']
            d=df['Discussion']
            e=df['Project']
            list_Total=array_creater(a)
            list_Learning=array_creater(b)
            list_R_and_D=array_creater(c)
            list_Discussion=array_creater(d)
            list_Project=array_creater(e)
            def converter(l1):
                l2=[]
                l5=[]
                for i in l1:
                    l3=i.split(':')
                    l4=[]
                    for j in l3:
                        l4.append(int(j))
                    sum=0
                    for k in l4:
                        if l4.index(k)==0:
                            sum+=k
                        if l4.index(k)==1:
                            sum+=(k/60)
                        if l4.index(k)==2:
                            sum+=(k/3600)
                    l5.append(sum)
                return l5
            Total=converter(list_Total)
            Learning=converter(list_Learning)
            R_and_D=converter(list_R_and_D)
            Discussion=converter(list_Discussion)
            Project=converter(list_Project)

            week1=[]
            week2=[]
            week3=[]
            week4=[]
            
            for i in range(4):
                if i==0:
                    week1.append(sum(Total[0:7])/len(Total[0:7]))
                    week1.append(sum(Learning[0:7])/len(Learning[0:7]))
                    week1.append(sum(R_and_D[0:7])/len(R_and_D[0:7]))
                    week1.append(sum(Discussion[0:7])/len(Discussion[0:7]))
                    week1.append(sum(Project[0:7])/len(Project[0:7]))
                elif i==1:
                    week2.append(sum(Total[7:14])/len(Total[7:14]))
                    week2.append(sum(Learning[7:14])/len(Learning[7:14]))
                    week2.append(sum(R_and_D[7:14])/len(R_and_D[7:14]))
                    week2.append(sum(Discussion[7:14])/len(Discussion[7:14]))
                    week2.append(sum(Project[7:14])/len(Project[7:14]))
                elif i==2:
                    week3.append(sum(Total[14:21])/len(Total[14:21]))
                    week3.append(sum(Learning[14:21])/len(Learning[14:21]))
                    week3.append(sum(R_and_D[14:21])/len(R_and_D[14:21]))
                    week3.append(sum(Discussion[14:21])/len(Discussion[14:21]))
                    week3.append(sum(Project[14:21])/len(Project[14:21]))
                else:
                    week4.append(sum(Total[21:])/len(Total[21:]))
                    week4.append(sum(Learning[21:])/len(Learning[21:]))
                    week4.append(sum(R_and_D[21:])/len(R_and_D[21:]))
                    week4.append(sum(Discussion[21:])/len(Discussion[21:]))
                    week4.append(sum(Project[21:])/len(Project[21:]))
            if num==0:
                week=week1
            elif num==1:
                week=week2
            elif num==2:
                week=week3
            elif num==3:
                week=week4
    

            x_axis=['Total','Learning','R&D','Discussion','Project']
            x_pos=np.arange(len(x_axis))
            width=0.10   
            plt.bar(x_pos,week,width=width)    
            plt.xticks(x_pos,x_axis)
            plt.ylabel('Working Hours')
            plt.title(name+' week'+str( num+1))
            plt.grid()
            plt.ylim(0,15)    
            plt.savefig("E:\\AtharvED\\AI\\{}bar.pdf".format(name),bbox_inches='tight',pad_inches=1)    
            plt.close()
            week_label=['Learning','R&D','Discussion','Project']
            plt.pie(week[1:],labels=week_label,autopct='%0.2f%%',shadow=True)
            plt.title(name+' week'+str( num)+' report')
            plt.savefig("E:\\AtharvED\\AI\\{}pie.pdf".format(name),bbox_inches='tight',pad_inches=1)
            plt.close()
            pdfs=["E:\\AtharvED\\AI\\{}bar.pdf".format(name),"E:\\AtharvED\\AI\\{}pie.pdf".format(name)]
            merger=PdfFileMerger()
            for pdf in pdfs:
                merger.append(pdf)
            merger.write("E:\\AtharvED\\AI\\{}week.pdf".format(name))

            #time.sleep(20)
            msg4 = QtWidgets.QMessageBox()
            msg4.setIcon(QMessageBox.Information)
            msg4.setText("Weekly Report has been started to Generate")
            msg4.setWindowTitle("Message")
            msg4.exec_()
        
    #to view the generated pdf
    def viewpdf(self):
        import subprocess
        import webbrowser
        k=self.comboBox_3.currentIndex()
        if k==0:
            subprocess.Popen(['Akashraj Bhat.pdf'],shell=True)
            #webbrowser.open_new('akashrajweek.pdf')           
        elif k==1:  
            subprocess.Popen(['Anarghya S R.pdf'],shell=True)
            #webbrowser.open_new('anarghyaweek.pdf')            
        elif k==2:
            subprocess.Popen(['Anush Laila.pdf'],shell=True)
            #webbrowser.open_new('anushweek.pdf')            
        elif k==3:
            subprocess.Popen(['Pranathi Acharya.png'],shell=True)
            #webbrowser.open_new('pranathiweek.pdf')            
        elif k==4:
            subprocess.Popen(['Prathik Nayak.pdf'],shell=True)
            #webbrowser.open_new('prathikweek.pdf')            
        elif k==5:
            subprocess.Popen(['Vanshika Shenoy.pdf'],shell=True)
            #webbrowser.open_new('vanshikaweek.pdf')            
        elif k==6:
            subprocess.Popen(['Vikas.pdf'],shell=True)
            #webbrowser.open_new('vikasweek.pdf')
        elif k==7:
            subprocess.Popen(['Abhishek Dileep.pdf'],shell=True)
            #webbrowser.open_new('abhishekweek.pdf')
        elif k==8:
            subprocess.Popen(['Akshatha.pdf'],shell=True)
            #webbrowser.open_new('akshathaweek.pdf')
        elif k==9:
            subprocess.Popen(['Aman Kumar Srivatsav.pdf'],shell=True)
            #webbrowser.open_new('amanweek.pdf')
        elif k==10:
            subprocess.Popen(['Anjali.pdf'],shell=True)
            #webbrowser.open_new('anjaliweek.pdf')
        elif k==11:
            subprocess.Popen(['Ankith Bhandary.pdf'],shell=True)
            #webbrowser.open_new('ankithweek.pdf')
        elif k==12:
            subprocess.Popen(['Aravind B R.pdf'],shell=True)
            #webbrowser.open_new('aravindaweek.pdf')
        elif k==13:
            subprocess.Popen(['Avish Shetty.pdf'],shell=True)
            #webbrowser.open_new('avishweek.pdf')
        elif k==14:
            subprocess.Popen(['Basangouda Patil.pdf'],shell=True)
            #webbrowser.open_new('basangoudaweek.pdf')
        elif k==15:
            subprocess.Popen(['Deekshith Prabhu.pdf'],shell=True)
            #webbrowser.open_new('deekshithweek.pdf')
        elif k==16:
            subprocess.Popen(['Harshitha G S .pdf'],shell=True)
            #webbrowser.open_new('harshithaweek.pdf')
        elif k==17:
            subprocess.Popen(['Josvin.pdf'],shell=True)
            #webbrowser.open_new('josvinweek.pdf')
        elif k==18:
            subprocess.Popen(['Keerthana.pdf'],shell=True)
            #webbrowser.open_new('vikasweek.pdf')
        elif k==19:
            subprocess.Popen(['Leeladhar Shetty.pdf'],shell=True)
            #webbrowser.open_new('leeladharweek.pdf')
        elif k==20:
            subprocess.Popen(['Meghana.pdf'],shell=True)
            #webbrowser.open_new('meghanaweek.pdf')
        elif k==21:
            subprocess.Popen(['Mokshith S Pergade.pdf'],shell=True)
            #webbrowser.open_new('mokshithweek.pdf')
        elif k==22:
            subprocess.Popen(['Namya Shetty.pdf'],shell=True)
            #webbrowser.open_new('namyaweek.pdf')
        elif k==23:
            subprocess.Popen(['Neha U.pdf'],shell=True)
            #webbrowser.open_new('nehaweek.pdf')
        elif k==24:
            subprocess.Popen(['Nidish Rao.pdf'],shell=True)
            #webbrowser.open_new('nidhishweek.pdf')
        elif k==25:
            subprocess.Popen(['Poornima.pdf'],shell=True)
            #webbrowser.open_new('poornimaweek.pdf')
        elif k==26:
            subprocess.Popen(['Pramod Shet.pdf'],shell=True)
            #webbrowser.open_new('pramodweek.pdf')
        elif k==27:
            subprocess.Popen(['Prasidda Hegde.pdf'],shell=True)
            #webbrowser.open_new('prasiddaweek.pdf')
        elif k==28:
            subprocess.Popen(['Prathiksha.pdf'],shell=True)
            #webbrowser.open_new('prathikshaweek.pdf')
        elif k==29:
            subprocess.Popen(['Praveen Nayak.pdf'],shell=True)
            #webbrowser.open_new('praveenweek.pdf')
        elif k==30:
            subprocess.Popen(['Preetham G S.pdf'],shell=True)
            #webbrowser.open_new('preethamweek.pdf')
        elif k==31:
            subprocess.Popen(['Ranjitha A S.pdf'],shell=True)
            #webbrowser.open_new('ranjithaweek.pdf')
        elif k==32:
            subprocess.Popen(['Rishabh Gujarati.pdf'],shell=True)
            #webbrowser.open_new('rishabhweek.pdf')
        elif k==33:
            subprocess.Popen(['S R Udith.pdf'],shell=True)
            #webbrowser.open_new('udithweek.pdf')
        elif k==34:
            subprocess.Popen(['Sameer G.pdf'],shell=True)
            #webbrowser.open_new('sameerweek.pdf')
        elif k==35:
            subprocess.Popen(['Sharath Hulekal.pdf'],shell=True)
            #webbrowser.open_new('sharathweek.pdf')
        elif k==36:
            subprocess.Popen(['Shashank H S.pdf'],shell=True)
            #webbrowser.open_new('shashankweek.pdf')
        elif k==37:
            subprocess.Popen(['Shreya R.pdf'],shell=True)
            #webbrowser.open_new('shreyaweek.pdf')
        elif k==38:
            subprocess.Popen(['Shreyas S.pdf'],shell=True)
            #webbrowser.open_new('shreyasweek.pdf')
        elif k==39:
            subprocess.Popen(['Shrinivas Anand Kamath.pdf'],shell=True)
            #webbrowser.open_new('shrinivasweek.pdf')
        elif k==40:
            subprocess.Popen(['Shubham.pdf'],shell=True)
            #webbrowser.open_new('shubhamweek.pdf')
        elif k==41:
            subprocess.Popen(['Sudhanva Acharya.pdf'],shell=True)
            #webbrowser.open_new('sudhanvaweek.pdf')
        elif k==42:
            subprocess.Popen(['Sushmita Shetty.pdf'],shell=True)
            #webbrowser.open_new('sushmithaweek.pdf')
        elif k==43:
            subprocess.Popen(['Vadiraj.pdf'],shell=True)
            #webbrowser.open_new('vadirajweek.pdf')
        elif k==44:
            subprocess.Popen(['Varsha  G D.pdf'],shell=True)
            #webbrowser.open_new('varshaweek.pdf')
        elif k==45:
            subprocess.Popen(['Vidhin.pdf'],shell=True)
            #webbrowser.open_new('vidhinweek.pdf')
        elif k==46:
            subprocess.Popen(['Vignesh Kini.pdf'],shell=True)
            #webbrowser.open_new('vighneshweek.pdf')
        elif k==47:
            subprocess.Popen(['Vijetha.pdf'],shell=True)
            #webbrowser.open_new('vijethaweek.pdf')
        elif k==48:
            subprocess.Popen(['Vineeth D Shetty.pdf'],shell=True)
            #webbrowser.open_new('vineethweek.pdf')
        elif k==49:
            subprocess.Popen(['Vrujesh H M.pdf'],shell=True)
            #webbrowser.open_new('vrujeshweek.pdf')
        elif k==50:
            subprocess.Popen(['Yogitha.pdf'],shell=True)
            #webbrowser.open_new('yogithaweek.pdf')
        elif k==51:
            subprocess.Popen(['Dhanraj.pdf'],shell=True)
            #webbrowser.open_new('yogithaweek.pdf')
            
            
        
    #to mail the weekly report to individuals
    def weekmail(self):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        l=self.comboBox_4.currentIndex()
            
        if l==0:
            email_send = "akashrajpbhat@gmail.com"  
            filename ='akashweek.pdf'
        elif l==1:
            email_send = "anarghyasr2000@gmail.com"       
            filename ='anarghyaweek.pdf'            
        elif l==2:
            email_send = "anush.laila.22@gmail.com"  
            filename ='anushweek.pdf'            
        elif l==3:
            email_send = "pranathiacharya1@gmail.com"        
            filename ='pranathiweek.pdf'            
        elif l==4:
            email_send = "prathiknayak03@gmail.com"
            filename ='prathikweek.pdf'            
        elif l==5:   
            email_send = "Vanshikashenoy07@gmail.com"
            filename ='vanshikaweek.pdf'           
        elif l==6:
            email_send = "vikaspoojary110@gmail.com"      
            filename ='vikasweek.pdf'
        elif l==7:            
            email_send = "Abhishekdileep99@gmail.com"
            filename ='abhishekweek.pdf'
        elif l==8:
            email_send = "akshatharao532@gmail.com" 
            filename ='akshathaweek.pdf'
        elif l==9:            
            email_send = "amansrivastav715@gmail.com"  
            filename ='amanweek.pdf'
        elif l==10:           
            email_send = "anjalipmadhyastha@gmail.com"  
            filename ='anjaliweek.pdf'
        elif l==11:        
            email_send = "ankithbhandary8@gmail.com"  
            filename ='ankithweek.pdf'
        elif l==12:            
            email_send = "arvikonoha@gmail.com"  
            filename ='aravindaweek.pdf'
        elif l==13:
            email_send = "avishvshetty@gmail.com"  
            filename ='avishweek.pdf'
        elif l==14:           
            email_send = "basanagoudap9141@gmail.com"  
            filename ='basangoudaweek.pdf'
        elif l==15:            
            email_send = "Deekshithprabhu284@gmail.com"  
            filename ='deekshithweek.pdf'
        elif l==16:            
            email_send = "harshithagsuresh97@gmail.com"  
            filename ='harshithaweek.pdf'
        elif l==17:            
            email_send = "josvincorda@gmail.com"
            filename ='josvinweek.pdf'
        elif l==18:           
            email_send = "puranik.keerthana@gmail.com"  
            filename ='keerthanaweek.pdf'
        elif l==19:            
            email_send = "leeladharabhijeeth21@yahoo.com"  
            filename ='leeladharweek.pdf'
        elif l==20:            
            email_send = "Shettymeghana32@gmail.com"  
            filename ='meghanaweek.pdf'
        elif l==21:           
            email_send = "smokshithpergade@gmail.com"  
            filename ='mokshithweek.pdf'
        elif l==22:            
            email_send = "namyashetty2001@gmail.com"  
            filename ='namyaweek.pdf'
        elif l==23:            
            email_send = "nehauday2000@gmail.com" 
            filename ='nehaweek.pdf'
        elif l==24:            
            email_send = "nidishnrao@gmail.com"  
            filename ='nidhishweek.pdf'
        elif l==25:          
            email_send = "poornimadakshay26@gmail.com"  
            filename ='poornimaweek.pdf'
        elif l==26:            
            email_send = "pramodshet109@gmail.com"  
            filename ='pramodweek.pdf'
        elif l==27:            
            email_send = "hegdeprasidh6@gmail.com"  
            filename ='prasiddaweek.pdf'
        elif l==28:            
            email_send = "Prathikshau0987@gmail.com"  
            filename ='prathikshaweek.pdf'
        elif l==29:            
            email_send = "praveensnayak12@gmail.com"
            filename ='praveenweek.pdf'
        elif l==30:           
            email_send = "shettigarpreetham15@gmail.com"  
            filename ='preethamweek.pdf'
        elif l==31:           
            email_send = "ranjitha.as.1998@gmail.com"  
            filename ='ranjithaweek.pdf'
        elif l==32:           
            email_send = "rishabhgujarati@gmail.com" 
            filename ='rishabhweek.pdf'
        elif i==33:           
            email_send = "srudith14@gmail.com"  
            filename ='udithweek.pdf'
        elif l==34:          
            email_send = "sameergp01@gmail.com"  
            filename ='sameerweek.pdf'
        elif i==35:            
            email_send = "sharathhulekal@gmail.com"  
            filename ='sharathweek.pdf'
        elif l==36:           
            email_send = "shashankhs333@gmail.com"
            filename ='shashankweek.pdf'
        elif l==37:            
            email_send = "shreyar490@gmail.com"  
            filename ='shreyaweek.pdf'
        elif l==38:            
            email_send = "shreyasmnglr9@gmail.com"  
            filename ='shreyasweek.pdf'
        elif l==39:           
            email_send = "kamathanand100@gmail.com"
            filename ='shrinivasweek.pdf'
        elif l==40:            
            email_send = "shubhamparmar262@gmail.com"  
            filename ='shubhamweek.pdf'
        elif l==41:            
            email_send = "sudhanva.udupi55@gmail.com"  
            filename ='sudhanvaweek.pdf'
        elif l==42:            
            email_send = "sushmitashetty2017@gmail.com"  
            filename ='sushmithaweek.pd'
        elif l==43:            
            email_send = "bvadirajatantry413@gmail.com"  
            filename ='vadirajweek.pdf'
        elif l==44:            
            email_send = "varshagundoomane@gmail.com"  
            filename ='varshaweek.pdf'
        elif l==45:           
            email_send = "vidhinpatel7@gmail.com" 
            filename ='vidhinweek.pdf'
        elif l==46:            
            email_send = "vigneshkini2000@gmail.com"
            filename ='vighneshweek.pdf'
        elif l==47:            
            email_send = "vijethap803@gmail.com" 
            filename ='vijethaweek.pdf'
        elif l==48: 
            email_send = "Vineethshetty289@gmail.com"  
            filename ='vineethweek.pdf'
        elif l==49:            
            email_send = "vru27091973@gmail.com"  
            filename ='vrujeshweek.pdf'
        elif l==50:            
            email_send = "yogithasnaik123@gmail.com"
            filename ='yogithaweek.pdf'
        elif l==50:            
            email_send = "dhanrajdeeru@gmail.com"
            filename ='Dhanrajweek.pdf'
            
        email_user = 'Athrvservices@gmail.com'      # from: mail id
        email_password = 'april@2020'
        subject = 'Weekly Performance Report'
        
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        
        body = 'This is your weekly Performance Report'
        msg.attach(MIMEText(body,'plain'))        
        attachment = open(filename, "rb")
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)
        server.sendmail(email_user,email_send,text)
        server.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Report Generator"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Akashraj"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Akashraj"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Anargya"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Anush"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Pranathi"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Prathik"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Vanshika"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Vikas"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Abhishek Dileep"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Akshatha"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Aman"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Anjali"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Ankith"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Aravinda"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Avish"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Basanagouda"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Deekshith"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Harshitha"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Josvin"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Keerthana"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Leeladhar"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Meghana"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Mokshith"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Namya"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Neha"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Nidhish"))
        self.comboBox.setItemText(25, _translate("MainWindow", "Poornima"))
        self.comboBox.setItemText(26, _translate("MainWindow", "Pramod"))
        self.comboBox.setItemText(27, _translate("MainWindow", "Prasidda"))
        self.comboBox.setItemText(28, _translate("MainWindow", "Prathiksha"))
        self.comboBox.setItemText(29, _translate("MainWindow", "Praveen"))
        self.comboBox.setItemText(30, _translate("MainWindow", "Preetham"))
        self.comboBox.setItemText(31, _translate("MainWindow", "Ranjitha"))
        self.comboBox.setItemText(32, _translate("MainWindow", "Rishabh"))
        self.comboBox.setItemText(33, _translate("MainWindow", "Udith"))
        self.comboBox.setItemText(34, _translate("MainWindow", "Sameer"))
        self.comboBox.setItemText(35, _translate("MainWindow", "Sharath"))
        self.comboBox.setItemText(36, _translate("MainWindow", "Shashank"))
        self.comboBox.setItemText(37, _translate("MainWindow", "Shreya R"))
        self.comboBox.setItemText(38, _translate("MainWindow", "Shreyas"))
        self.comboBox.setItemText(39, _translate("MainWindow", "Shrinivas"))
        self.comboBox.setItemText(40, _translate("MainWindow", "Shubham"))
        self.comboBox.setItemText(41, _translate("MainWindow", "Sudhanva"))
        self.comboBox.setItemText(42, _translate("MainWindow", "Sushmitha"))
        self.comboBox.setItemText(43, _translate("MainWindow", "Vadiraj"))
        self.comboBox.setItemText(44, _translate("MainWindow", "Varsha"))
        self.comboBox.setItemText(45, _translate("MainWindow", "Vidhin"))
        self.comboBox.setItemText(46, _translate("MainWindow", "Vighnesh"))
        self.comboBox.setItemText(47, _translate("MainWindow", "Vijetha"))        
        self.comboBox.setItemText(48, _translate("MainWindow", "Vineeth"))
        self.comboBox.setItemText(49, _translate("MainWindow", "Vrujesh"))
        self.comboBox.setItemText(50, _translate("MainWindow", "Yogitha"))
        self.comboBox.setItemText(51, _translate("MainWindow", "Dhanraj"))
        self.label_6.setText(_translate("MainWindow", "Developed and Maintained by : Athrv-Ed Artificial Intelligence Team"))
        self.label_4.setText(_translate("MainWindow", "Select the Participants to View the Report"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "Week 1"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Week 1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Week 2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Week 3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Week 4"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate Monthly Report"))
        self.label_5.setText(_translate("MainWindow", "Select the Participants to mail the Weekly Report"))
        self.label_3.setText(_translate("MainWindow", "Select the Participants to mail the Monthly Report"))
        self.label_7.setText(_translate("MainWindow", "Select the Week to generate Report"))
        self.pushButton_4.setText(_translate("MainWindow", "Mail All"))
        self.pushButton_5.setText(_translate("MainWindow", "Mail All"))
        self.comboBox_4.setCurrentText(_translate("MainWindow", "Akashraj"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Akashraj"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Anargya"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Anush"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Pranathi"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Prathik"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Vanshika"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "Vikas"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "Abhishek Dileep"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "Akshatha"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "Aman"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "Anjali"))
        self.comboBox_4.setItemText(11, _translate("MainWindow", "Ankith"))
        self.comboBox_4.setItemText(12, _translate("MainWindow", "Aravinda"))
        self.comboBox_4.setItemText(13, _translate("MainWindow", "Avish"))
        self.comboBox_4.setItemText(14, _translate("MainWindow", "Basanagouda"))
        self.comboBox_4.setItemText(15, _translate("MainWindow", "Deekshith"))
        self.comboBox_4.setItemText(16, _translate("MainWindow", "Harshitha"))
        self.comboBox_4.setItemText(17, _translate("MainWindow", "Josvin"))
        self.comboBox_4.setItemText(18, _translate("MainWindow", "Keerthana"))
        self.comboBox_4.setItemText(19, _translate("MainWindow", "Leeladhar"))
        self.comboBox_4.setItemText(20, _translate("MainWindow", "Meghana"))
        self.comboBox_4.setItemText(21, _translate("MainWindow", "Mokshith"))
        self.comboBox_4.setItemText(22, _translate("MainWindow", "Namya"))
        self.comboBox_4.setItemText(23, _translate("MainWindow", "Neha"))
        self.comboBox_4.setItemText(24, _translate("MainWindow", "Nidhish"))
        self.comboBox_4.setItemText(25, _translate("MainWindow", "Poornima"))
        self.comboBox_4.setItemText(26, _translate("MainWindow", "Pramod"))
        self.comboBox_4.setItemText(27, _translate("MainWindow", "Prasidda"))
        self.comboBox_4.setItemText(28, _translate("MainWindow", "Prathiksha"))
        self.comboBox_4.setItemText(29, _translate("MainWindow", "Praveen"))
        self.comboBox_4.setItemText(30, _translate("MainWindow", "Preetham"))
        self.comboBox_4.setItemText(31, _translate("MainWindow", "Ranjitha"))
        self.comboBox_4.setItemText(32, _translate("MainWindow", "Rishabh"))
        self.comboBox_4.setItemText(33, _translate("MainWindow", "Udith"))
        self.comboBox_4.setItemText(34, _translate("MainWindow", "Sameer"))
        self.comboBox_4.setItemText(35, _translate("MainWindow", "Sharath"))
        self.comboBox_4.setItemText(36, _translate("MainWindow", "Shashank"))
        self.comboBox_4.setItemText(37, _translate("MainWindow", "Shreya R"))
        self.comboBox_4.setItemText(38, _translate("MainWindow", "Shreyas"))
        self.comboBox_4.setItemText(39, _translate("MainWindow", "Shrinivas"))
        self.comboBox_4.setItemText(40, _translate("MainWindow", "Shubham"))
        self.comboBox_4.setItemText(41, _translate("MainWindow", "Sudhanva"))
        self.comboBox_4.setItemText(42, _translate("MainWindow", "Sushmitha"))
        self.comboBox_4.setItemText(43, _translate("MainWindow", "Vadiraj"))
        self.comboBox_4.setItemText(44, _translate("MainWindow", "Varsha"))
        self.comboBox_4.setItemText(45, _translate("MainWindow", "Vidhin"))
        self.comboBox_4.setItemText(46, _translate("MainWindow", "Vighnesh"))
        self.comboBox_4.setItemText(47, _translate("MainWindow", "Vijetha"))        
        self.comboBox_4.setItemText(48, _translate("MainWindow", "Vineeth"))
        self.comboBox_4.setItemText(49, _translate("MainWindow", "Vrujesh"))
        self.comboBox_4.setItemText(50, _translate("MainWindow", "Yogitha"))
        self.comboBox_4.setItemText(51, _translate("MainWindow", "Dhanraj"))
        self.comboBox_3.setCurrentText(_translate("MainWindow", "Akashraj"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Akashraj"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Anargya"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Anush"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Pranathi"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Prathik"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Vanshika"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Vikas"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Abhishek Dileep"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Akshatha"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "Aman"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Anjali"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Ankith"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "Aravinda"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "Avish"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "Basanagouda"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "Deekshith"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "Harshitha"))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "Josvin"))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "Keerthana"))
        self.comboBox_3.setItemText(19, _translate("MainWindow", "Leeladhar"))
        self.comboBox_3.setItemText(20, _translate("MainWindow", "Meghana"))
        self.comboBox_3.setItemText(21, _translate("MainWindow", "Mokshith"))
        self.comboBox_3.setItemText(22, _translate("MainWindow", "Namya"))
        self.comboBox_3.setItemText(23, _translate("MainWindow", "Neha"))
        self.comboBox_3.setItemText(24, _translate("MainWindow", "Nidhish"))
        self.comboBox_3.setItemText(25, _translate("MainWindow", "Poornima"))
        self.comboBox_3.setItemText(26, _translate("MainWindow", "Pramod"))
        self.comboBox_3.setItemText(27, _translate("MainWindow", "Prasidda"))
        self.comboBox_3.setItemText(28, _translate("MainWindow", "Prathiksha"))
        self.comboBox_3.setItemText(29, _translate("MainWindow", "Praveen"))
        self.comboBox_3.setItemText(30, _translate("MainWindow", "Preetham"))
        self.comboBox_3.setItemText(31, _translate("MainWindow", "Ranjitha"))
        self.comboBox_3.setItemText(32, _translate("MainWindow", "Rishabh"))
        self.comboBox_3.setItemText(33, _translate("MainWindow", "Udith"))
        self.comboBox_3.setItemText(34, _translate("MainWindow", "Sameer"))
        self.comboBox_3.setItemText(35, _translate("MainWindow", "Sharath"))
        self.comboBox_3.setItemText(36, _translate("MainWindow", "Shashank"))
        self.comboBox_3.setItemText(37, _translate("MainWindow", "Shreya R"))
        self.comboBox_3.setItemText(38, _translate("MainWindow", "Shreyas"))
        self.comboBox_3.setItemText(39, _translate("MainWindow", "Shrinivas"))
        self.comboBox_3.setItemText(40, _translate("MainWindow", "Shubham"))
        self.comboBox_3.setItemText(41, _translate("MainWindow", "Sudhanva"))
        self.comboBox_3.setItemText(42, _translate("MainWindow", "Sushmitha"))
        self.comboBox_3.setItemText(43, _translate("MainWindow", "Vadiraj"))
        self.comboBox_3.setItemText(44, _translate("MainWindow", "Varsha"))
        self.comboBox_3.setItemText(45, _translate("MainWindow", "Vidhin"))
        self.comboBox_3.setItemText(46, _translate("MainWindow", "Vighnesh"))
        self.comboBox_3.setItemText(47, _translate("MainWindow", "Vijetha"))        
        self.comboBox_3.setItemText(48, _translate("MainWindow", "Vineeth"))
        self.comboBox_3.setItemText(49, _translate("MainWindow", "Vrujesh"))
        self.comboBox_3.setItemText(50, _translate("MainWindow", "Yogitha"))
        self.comboBox_3.setItemText(51, _translate("MainWindow", "Dhanraj"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
