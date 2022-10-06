import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("杨辉三角")
win.geometry("900x600")

l = tk.Label(win, text="请输入行数", width=13, height=1, font=("Arial", 20))
l.pack()

e = tk.Entry(win, font=("Arial", 14), width=13)
e.pack()

def yf_gen():
    t.delete(1.0, "end")
    try:
        line = int(e.get())
        b = []
        for i in range(1, line + 1):
            if i <= 2:
                b.append(1)
                t.insert("end", str(b))
                t.insert("end", "\n")
            else:
                r = [b[e] + b[e + 1] for e in range(0, len(b) - 1)]
                b = [1] + r + [1]
                c = "     (a+b)**{0}".format(i-1)
                t.insert("end", str(b)+c)
                t.insert("end", "\n")
    except ValueError:
        messagebox.showinfo(title="提示", message="请输入行数")


b = tk.Button(win, width=13, height=2, text="查看结果", bg="blue",fg="white", command=yf_gen)
b.pack()

t = tk.Text(win, width=900, height=400, font=("Arial", 14))
t.pack()

win.mainloop()
