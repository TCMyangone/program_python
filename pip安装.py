import os
pip = input("请输入要安装的库: ")
os.system("pip install %s -i https://pypi.douban.com/simple"%pip)
_ = input("按回车以退出")