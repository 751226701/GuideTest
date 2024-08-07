# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 16:55
# @File :tkinter27
# @Project : GuideTest
import tkinter.messagebox
from tkinter import *

win = Tk()
win.config(bg='#87CEEB')
win.title("Study")
win.geometry('450x350+300+200')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

def menuCommand():
    tkinter.messagebox.showinfo("主菜单栏", "你正在使用主菜单栏")

main_menu = Menu(win)
main_menu.add_command(label="文件", command=menuCommand)
main_menu.add_command(label="编辑", command=menuCommand)
main_menu.add_command(label="格式", command=menuCommand)
main_menu.add_command(label="查看", command=menuCommand)
main_menu.add_command(label="帮助", command=menuCommand)

win.config(menu=main_menu)
win.mainloop()




































