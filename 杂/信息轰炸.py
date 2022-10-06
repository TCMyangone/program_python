from tkinter import *
import tkinter as tk
import win32gui
import win32con
import win32clipboard as w

window = tk.Tk()
window.title('QQ信息轰炸')
window.geometry('500x300')

e1 = tk.Label(window, text='呱呱呱呱', bg='green', font=('Arial', 12)).grid(row=0, column=0)
e3 = tk.Label(window, text='请输入循环次数', font=('Arial', 12)).grid(row=1, column=0)
e4 = tk.Label(window, text='请输入QQ备注名', font=('Arial', 12)).grid(row=2, column=0)
e5 = tk.Label(window, text='请输入发送内容', font=('Arial', 12)).grid(row=3, column=0)


def hit_me():
    n = int(N.get())  # 请输入循环次数
    # print(a)
    name = Name.get()  # 请输入QQ备注名
    mgs = Mgs.get()  # 请输入发送内容

    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, mgs)
    w.CloseClipboard()
    # 获取窗口句柄
    handle = win32gui.FindWindow(None, name)
    for i in range(0, n):
        # 填充消息
        win32gui.SendMessage(handle, 770, 0, 0)
        # 回车发送消息`
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


N = StringVar()
Name = StringVar()
Mgs = StringVar()

e2 = tk.Entry(window, textvariable=N, font=('Arial', 10)).grid(row=1, column=2)  # 显示成明文形式
e6 = tk.Entry(window, textvariable=Name, font=('Arial', 10)).grid(row=2, column=2)
e7 = tk.Entry(window, textvariable=Mgs, font=('Arial', 10)).grid(row=3, column=2)

b = tk.Button(window, text='轰炸', font=('Arial', 12), width=10, height=1, command=hit_me).grid(row=4, column=2)

window.mainloop()
