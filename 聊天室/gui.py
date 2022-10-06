# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(631, 490)
        MainWindow.setFixedSize(631, 490)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setStyleSheet(u"QMenuBar, QMenu{\n"
"	font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"	font-size:16px;\n"
"	color: #1d649c;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"	font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"	font-size:16px;\n"
"	color: black;\n"
"	background-color: #aaffff\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"	background-color: #aaffff;\n"
"	font-size: 16px;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"	font-size: 19px;\n"
"	color: #1d649c;\n"
"}\n"
"\n"
"*{\n"
"	border:1px solid #1d649c;\n"
"}")
        self.actionasdf = QAction(MainWindow)
        self.actionasdf.setObjectName(u"actionasdf")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 511, 301))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        self.textBrowser.setFont(font)
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(510, 0, 121, 301))
        self.textBrowser_2.setStyleSheet(u"")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 300, 541, 141))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 300, 101, 141))
        self.pushButton.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 631, 29))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.actionasdf.setText(QCoreApplication.translate("MainWindow", u"asdf ", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
    # retranslateUi

