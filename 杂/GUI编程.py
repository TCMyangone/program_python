import tkinter as tk

window = tk.Tk()
window.title("我的窗口")
window.geometry("500x300")

e1 = tk.Entry(window, show="", font=("Arial",14))
e1.pack()

def insert_point():
    var = e1.get()
    t.insert("insert", var)

def insert_end():
    var = e1.get()
    t.insert("end", var)

b1 = tk.Button(window, text="Insert point", width=10, height=2, command=insert_point, anchor="center")
b2 = tk.Button(window, text="Insert end", width=10, height=2, command=insert_end)
b1.pack()
b2.pack()

t = tk.Text(window, height=3)
t.pack()

window.mainloop()
