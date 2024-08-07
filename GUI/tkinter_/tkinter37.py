# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 10:25
# @File :tkinter37
# @Project : GuideTest
from tkinter import *

win = Tk()
win.title("C语言中文网")
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

frame = Frame(win, relief=SUNKEN, borderwidth=2, width=450, height=250)
frame.pack(side=TOP, fill=BOTH, expand=1)

label1 = Label(frame, text="位置1", bg='blue', fg='white')
label1.place(x=40, y=40, width=60, height=30)

Label2 = Label(frame, text="位置2", bg='purple', fg='white')
Label2.place(x=180, y=80, anchor=NE, width=60, height=30)

Label3 = Label(frame, text="位置3", bg='green', fg='white')
# 设置水平起始位置相对于窗体水平距离的0.6倍，垂直的绝对距离为80，大小为60，30
Label3.place(relx=0.6, y=80, width=60, height=30)

Label4 = Label(frame, text="位置4", bg='gray', fg='white')
# 设置水平起始位置相对于窗体水平距离的0.01倍，垂直的绝对距离为80，并设置高度为窗体高度比例的0.5倍，宽度为80
Label4.place(relx=0.01, y=80, relheight=0.4, width=80)

win.mainloop()
