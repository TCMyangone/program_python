from PyQt5.QtWidgets import QApplication, QWidget
import sys

# 创建QApplication的实例
app = QApplication(sys.argv)
# 创建一个窗口
win = QWidget()
# 设置窗口尺寸
win.resize(400, 200)
# 移动窗口
win.move(300, 300)
# 设置窗口标题
win.setWindowTitle("PyQt5程序")
# 显示窗口
win.show()
# 不断刷新屏幕,程序主循环
sys.exit(app.exec_())
