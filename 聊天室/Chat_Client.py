import socket
import threading
import os
from time import sleep
import keyboard
import re
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtCore import *
from PySide2.QtGui import *
from gui import Ui_MainWindow
from login import Ui_Form



class Client():
    ''''一个客户端类'''
    def __init__(self):
        ''''初始化客户端信息'''
        self.host = '127.0.0.1'
        self.port = 0
        self.user_name = ''
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client = Client() #实例化客户端类

class Main(QMainWindow):
    '''一个主窗口类'''

    def __init__(self):
        '''初始化主窗口,继承QMainWindow'''
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.send_msg)
        self.ui.actionExit.triggered.connect(self.close)
        threading.Thread(target=self.recv_msg).start()
        threading.Thread(target=self.enter_send).start()

    def close(self):
        '''关闭程序'''
        os._exit(0)

    def send_msg(self):
        '''获取消息并发送消息'''
        sleep(0.1001)
        r = re.compile(r'.')
        self.text = self.ui.plainTextEdit.toPlainText()
        self.result = r.findall(self.text)
        print(self.result)
        if self.result:
            client.c.send(self.text.encode('utf-8'))
            sleep(0.1001)
            self.ui.plainTextEdit.clear()
        else:
            sleep(0.1001)
            self.ui.plainTextEdit.clear()

    def enter_send(self):
        '''实现回车键发送信息'''
        while True:
            keyboard.wait('enter')
            self.send_msg()

    def recv_msg(self):
        '''不断接收信息显示到屏幕'''
        while True:
            self.rec = client.c.recv(1024).decode('utf-8')
            self.ui.textBrowser.append(self.rec)
            self.ui.textBrowser.ensureCursorVisible()



class Login(QWidget):
    '''一个登陆界面的类'''
    def __init__(self):
        '''初始化,继承该界面所需的主窗口--QWidget'''
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.enter)        


    def enter(self):
        '''记录用户输入的信息并发送至服务端'''
        try:
            client.port, client.user_name = int(self.ui.lineEdit_3.text()), self.ui.lineEdit_4.text()
            client.c.connect((client.host, client.port))
            client.c.send(client.user_name.encode('utf-8'))
            self.main = Main()
            self.main.show()
            self.close()
        except ConnectionRefusedError:
            pass

    #重写移动事件
    def mouseMoveEvent(self, e: QMouseEvent):
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
    
    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True
    
    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

app = QApplication([])
main_window = Login()
main_window.show()
app.exec_()