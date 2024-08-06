# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 15:53
# @File :tkinter24
# @Project : GuideTest
from tkinter import *

win = Tk()
win.title("C语言中文网")
win.geometry('500x200')
win.resizable(False, False)
lb = Label(text='C语言中文网答疑辅导班', font=('微软雅黑', 18, 'bold'), fg='#CD7054')
lb.pack()
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

check1 = Checkbutton(win, text="Python", font=('微软雅黑', 15, 'bold'), onvalue=1, offvalue=0)
check2 = Checkbutton(win, text="C语言", font=('微软雅黑', 15, 'bold'), onvalue=1, offvalue=0)
check3 = Checkbutton(win, text="Java", font=('微软雅黑', 15, 'bold'), onvalue=1, offvalue=0)
check1.select()
check1.toggle()
check1.pack(side=LEFT)
check2.pack(side=LEFT)
check3.pack(side=LEFT)

win.mainloop()
