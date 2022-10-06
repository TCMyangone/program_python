import datetime

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLineEdit
import sys


class IdAge(QWidget):
    """管理GUI控件和相关功能的类"""

    def __init__(self):
        """初始化程序"""
        super().__init__()
        self.initUI()

    def initUI(self):
        """定义并显示各项控件"""
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("根据身份证号推测年龄")

        self.button = QPushButton("查看结果", self)
        self.button.setGeometry(115, 150, 70, 30)
        self.button.setToolTip("点击按钮查看年龄")
        self.button.clicked.connect(self.show_age)

        self.text = QLineEdit("在这里输入身份证号", self)
        self.text.setGeometry(80, 50, 150, 30)
        self.text.setFocus()
        self.text.selectAll()

        self.show()

    def show_age(self):
        """实现判断年龄的代码"""
        now_year = datetime.datetime.now().year
        now_month = datetime.datetime.now().month
        now_day = datetime.datetime.now().day

        id = self.text.text()
        user_year = int(id[6:10])
        user_month = int(id[10:12])
        user_day = int(id[12:14])

        if now_month >= user_month and now_day >= user_day:
            QMessageBox.about(self, '查看年龄', str(now_year - user_year) + "岁")
            self.text.setFocus()
            self.text.selectAll()
        else:
            QMessageBox.about(self, '查看年龄', str(now_year - user_year - 1) + "岁")
            self.text.setFocus()
            self.text.selectAll()


app = QApplication(sys.argv)
win = IdAge()
sys.exit(app.exec_())
