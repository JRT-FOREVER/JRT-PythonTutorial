import tkinter as tk
window = tk.Tk("My Window")
window.geometry('200x300')
var1 = tk.StringVar()
label = tk.Label(window, textvariable=var1, bg='red', width=30, height=2)
label.pack()
# print(type(var1))


# 下面是按钮的回调函数
def print2label():
    global var1  # 使用全局作用域的变量
    res = lb.get(lb.curselection())  # 获取光标指向的item
    var1.set(res)
button = tk.Button(window, text='print to the label', command=print2label, width=30, height=2)
button.pack()
var2 = tk.StringVar()  # var2是放在列表框当中的
var2.set((1, 2, 3, 4))  # 元组参数


lb = tk.Listbox(window, listvariable=var2)
lb.pack()
tuple_test = ['J', 'R', 'T']
for item in tuple_test:
    lb.insert('end', item)
lb.insert(1, 'JRT')
lb.insert(2, 'abc')
lb.delete(2)
window.mainloop()


