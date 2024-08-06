# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/2 9:55
# @File :tkinter06
# @Project : GuideTest

from tkinter import *

win = Tk()
win.config(bg='#8DB6CD')
win.title("Study")
win.geometry('400x300')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
txt = "C语言中文网，网址是：c.biancheng.net"
message = Message(win, text=txt, width=60, font=('微软雅黑', 10, 'bold'))
message.pack(side=LEFT)
win.mainloop()
