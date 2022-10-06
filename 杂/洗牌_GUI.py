import tkinter as tk
from tkinter import messagebox

# 创建窗口
window = tk.Tk()
window.title("完美洗牌")
window.geometry("1000x600")

# 创建标签
l = tk.Label(window, text="请输入牌数", width=13, height=1, font=("Arial", 20))
l.pack()

# 创建输入框
e = tk.Entry(window, font=("Arial", 14), width=13)
e.pack()


# 洗牌具体算法
def new_func():
    t.delete(1.0, "end")
    try:
        times = int(e.get())
        brand = list(range(0, times))
        brand_copy = brand.copy()
        frequency = 0
        t.insert("end", "还原过程\n")
        while True:
            brand_1 = brand[:int(times / 2)]
            brand_2 = brand[int(times / 2):]
            brand_3 = list(zip(brand_1, brand_2))
            brand.clear()
            brand = [e for i in brand_3 for e in i]
            frequency += 1
            t.insert("insert", str(brand))
            t.insert("end", '\n')
            if brand == brand_copy:
                t.insert("insert", '还原成功\n')
                t.insert("insert", '次数:' + str(frequency))
                break
    except ValueError:
        messagebox.showinfo(title="提示", message="请输入牌数")


# 创建按钮
b = tk.Button(window, width=13, height=2, text="查看结果", bg="blue", fg="white", command=new_func)
b.pack()

var = tk.StringVar()
t = tk.Text(window, width=1000, height=400, font=("Arial", 13))
t.pack()

# 不断刷新屏幕
window.mainloop()
