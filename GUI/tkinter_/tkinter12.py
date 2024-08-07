# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 9:58
# @File :tkinter12
# @Project : GuideTest
from tkinter import *

win = Tk()
win.geometry('300x300')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
frame = Frame(win)
def cal():
    res = "=" + str(eval(expression.get()))
    label.config(text=res)
label = Label(frame)
entry = Entry(frame)
expression = StringVar()
entry['textvariable'] = expression
button1 = Button(frame, text="等于", command=cal)
entry.focus()
frame.pack()
entry.pack()
label.pack(side='left')
button1.pack(side='right')
frame.mainloop()
















