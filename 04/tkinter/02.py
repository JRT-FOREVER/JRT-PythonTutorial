# 想法来自网络
import tkinter as tk
window = tk.Tk('My Window')
window.geometry('700x500')
entry = tk.Entry(window, show=None, width=30)  # 可以通过show=''来指定掩码
entry.pack()


def add2point():
    t.insert('insert', entry.get())  # insert模式用于在光标处插入


def add2end():
    t.insert('end', entry.get())  # end模式用于在尾部插入, 可以通过m.n模式来指定插入的行和列

bt1 = tk.Button(window, text='add to the point', bg='blue', width=15, height=2, command=add2point)
bt1.pack()
bt2 = tk.Button(window, text='add to the end', bg='green', width=15, height=2, command=add2end)
bt2.pack()
t = tk.Text(window, width=30, height=10)
t.pack()
window.mainloop()

