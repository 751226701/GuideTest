# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 13:55
# @File :tkinter19
# @Project : GuideTest
from tkinter import *

win = Tk()
win.title("Study")
win.geometry('400x180')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
# 创建滚动条
s = Scrollbar(win)
s.pack(side=RIGHT, fill=Y)
# 将 selectmode 设置为多选模式，并为Listbox控件添加滚动条
listbox1 = Listbox(win, selectmode=MULTIPLE, height=5, yscrollcommand=s.set)
for i, item in enumerate(range(1, 50)):
    listbox1.insert(i, item)
listbox1.pack()
s.config(command=listbox1.yview)
bt = Button(win, text="删除", command=lambda x=listbox1: x.delete(ACTIVE))
bt.pack(side=BOTTOM)
win.mainloop()
