# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 9:55
# @File :tkinter35
# @Project : GuideTest
from tkinter import *

win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('500x350+300+300')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

for i in range(10):
    for j in range(10):
        Button(win, text="(" + str(i) + "," + str(j) + ")", bg='#D1EEEE').grid(row=i, column=j)

Label(win, text="C语言中文网", fg='blue', font=('楷体', 12, 'bold')).grid(row=4, column=10)
win.mainloop()























