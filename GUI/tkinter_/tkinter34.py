# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 9:42
# @File :tkinter34
# @Project : GuideTest

from tkinter import *
win = Tk()
win.title("C语言中文网")
win.geometry('450x300+300+300')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

lb_red = Label(win, text="红色", bg="Red", fg='#ffffff', relief=GROOVE)
lb_red.pack()
lb_blue = Label(win, text="蓝色", bg="blue", fg='#ffffff', relief=GROOVE)
# 沿着水平方向填充，使用 pady 控制蓝色标签与其他标签的上下距离为 5 个像素
lb_blue.pack(fill=X, pady='5px')
lb_green = Label(win, text="绿色", bg="green", fg='#ffffff', relief=RAISED)
# 将 黄色标签所在区域都填充为黄色，当使用 fill 参数时，必须设置 expand = 1，否则不能生效
lb_green.pack(side=LEFT, expand=1, fill=BOTH)
win.mainloop()


























