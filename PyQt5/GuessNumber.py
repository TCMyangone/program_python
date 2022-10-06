import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
import random


class GuessNumber(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = random.randint(1, 100)

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("猜数字")
        self.setWindowIcon(QIcon("PyQt5/q.ico"))

        self.button_1 = QPushButton("猜一猜", self)
        self.button_1.setGeometry(115, 150, 70, 30)
        self.button_1.clicked.connect(self.showmessage)
        self.button_1.setToolTip("点击按钮猜数字")

        self.le = QLineEdit("在这里输入数字", self)
        self.le.selectAll()
        self.le.setFocus()
        self.le.setGeometry(80, 50, 150, 30)

        self.show()

    def showmessage(self):
        guess_number = int(self.le.text())

        if guess_number > self.num:
            QMessageBox.about(self, "看结果", "猜大了!")
            self.le.setFocus()
            self.le.selectAll()

        elif guess_number < self.num:
            QMessageBox.about(self, "看结果", "猜小了!")
            self.le.setFocus()
            self.le.selectAll()

        else:
            QMessageBox.about(self, "看结果", "答对了!,进入下一轮")
            self.num = random.randint(1, 100)
            self.le.clear()
            self.le.setFcous()
            self.le.selectAll()

    def close_event(self, event):
        reply = QMessageBox.question(self, "退出", "确认要退出吗", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
ico = GuessNumber()
sys.exit(app.exec_())
