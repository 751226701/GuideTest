# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 17:18
# @File :tkinter28
# @Project : GuideTest
import tkinter.messagebox
from tkinter import *

win = Tk()
win.config(bg='#87CEEB')
win.title("Study")
win.geometry('450x350+300+200')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

def menuCommand(event=None):
    tkinter.messagebox.showinfo("主菜单栏", "你正在使用下拉菜单功能")

main_menu = Menu(win)
file_menu = Menu(main_menu, tearoff=False)
file_menu.add_command(label="新建", command=menuCommand, accelerator="Ctrl+N")
file_menu.add_command(label="打开", command=menuCommand, accelerator="Ctrl+O")
file_menu.add_command(label="保存", command=menuCommand, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="退出", command=win.quit)

main_menu.add_cascade(label="文件", menu=file_menu)
win.config(menu=main_menu)

win.bind("<Control-n>", menuCommand)
win.bind("<Control-N>", menuCommand)
win.bind("<Control-o>", menuCommand)
win.bind("<Control-O>", menuCommand)
win.bind("<Control-s>", menuCommand)
win.bind("<Control-S>", menuCommand)
win.mainloop()
