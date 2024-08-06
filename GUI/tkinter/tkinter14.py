# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 10:33
# @File :tkinter14
# @Project : GuideTest
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Study")
win.geometry('400x300')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
# 创建一个文本控件
# width 一行可见的字符数；height 显示的行数
text = Text(win, width=50, height=10, undo=True, autoseparators=False)
text.grid()
# INSERT 光标处插入；END 末尾处插入
text.insert(INSERT, "Hello, world")
# 定义撤销和恢复方法，调用edit_undo()和 edit_redo()方法
def backout():
    text.edit_undo()
def regain():
    text.edit_redo()
Button(win, text="撤销", command=backout).grid(row=3, column=0, stick='w', padx=10, pady=5)
Button(win, text="恢复", command=regain).grid(row=3, column=0, stick='e', padx=10, pady=5)
win.mainloop()








