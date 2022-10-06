import tkinter as tk

window = tk.Tk()
window.title("登录")
window.geometry("500x300")

var = tk.StringVar()

l = tk.Label(window, textvariable=var, font=("Arial, 13"), width=10, height=1)
l.pack()

e1 = tk.Entry(window, show="", font=("Arial",14))
e2 = tk.Entry(window, show="*", font=("Arial",14))
e1.pack()
e2.pack()

user_name = "oysj123"
user_password = "oysj20061226"

def login():
    if user_name == e1.get() and user_password == e2.get():
        var.set("登陆成功")
    else:
        var.set("登陆失败")

b = tk.Button(window, text="登录", font=("Arial", 15), width=10, height=1, command=login)
b.pack()

window.mainloop()