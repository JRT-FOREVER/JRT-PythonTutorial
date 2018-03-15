import tkinter as tk
status = False
window = tk.Tk("my first window")
window.geometry('200x150')
var = tk.StringVar()
lb = tk.Label(window, textvariable=var, bg='red', font=('Arial', 12), width=15, height=2)
lb.pack()


def on_click():
    global status
    if not status:
        status = True
        var.set("I am clicked")
    else:
        status = False
        var.set("")

bt = tk.Button(window, text='click me', width=15, height=2, command=on_click)
bt.pack()
window.mainloop()  # 进入主循环

