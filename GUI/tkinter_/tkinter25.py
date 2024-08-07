# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 16:23
# @File :tkinter25
# @Project : GuideTest
from tkinter import *

win = Tk()
win.title("C语言中文网")
win.geometry('500x200')
win.resizable(False, False)
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
# 添加一个 Scale 控件，默认垂直方向，步长设置为 5，长度为200，滑动块的大小为 50，最后使用label参数文本
s = Scale(win, from_=100, to=0, resolution=5, length=200, sliderlength=20, label="压力控制")
s.pack()
win.mainloop()
