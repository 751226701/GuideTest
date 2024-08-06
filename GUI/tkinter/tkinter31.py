# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 8:45
# @File :tkinter31
# @Project : GuideTest
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("C语言中文网")
root.geometry('450x180+300+200')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

# 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
sbar1 = tk.Scrollbar(root)
sbar1.pack(side=RIGHT, fill=Y)
# 创建水平滚动条，默认为水平方向,当拖动窗口时会沿着X轴方向填充
sbar2 = Scrollbar(root, orient=HORIZONTAL)
sbar2.pack(side=BOTTOM, fill=X)
# 创建列表框控件,并添加两个滚动条（分别在垂直和水平方向），使用 set() 进行设置
mylist = tk.Listbox(root, xscrollcommand=sbar2.set, yscrollcommand=sbar1.set)
for i in range(30):
    mylist.insert(END, '第' + str(i+1)+'次:'+'C语言中文网，网址为：c.biancheng.net' + '\n')

mylist.pack(side=LEFT, fill=BOTH)
# 使用 command 关联控件的 yview、xview方法
sbar1.config(command=mylist.yview)
sbar2.config(command=mylist.xview)

root.mainloop()
























