import tkinter as tk
window = tk.Tk("My window")
window.geometry('500x400')
lb = tk.Label(window, width=30, height=2, bg='green')
lb.pack()
var = tk.StringVar()


def print2label():
    lb.config(text="%s was selevted" % var.get())  # 重新配置lb的属性
    
rb1 = tk.Radiobutton(window, command=print2label, variable=var, value='button1', text='button1')
rb1.pack()
rb2 = tk.Radiobutton(window, command=print2label, variable=var, value='button2', text='button1')
rb2.pack()
rb3 = tk.Radiobutton(window, command=print2label, variable=var, value='button3', text='button1')
rb3.pack()
window.mainloop()

