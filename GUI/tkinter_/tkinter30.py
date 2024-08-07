# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 19:45
# @File :tkinter30
# @Project : GuideTest
from tkinter import *

win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
# 创建一个菜单按钮
menu_btn = Menubutton(win, text='点击进行操作', relief='sunk')
menu_btn.grid(padx=195, pady=105)
file_menu = Menu(menu_btn, tearoff=False)

def func():
    print("test is ok!")

file_menu.add_command(label='新建', command=func)
file_menu.add_command(label='删除', command=func)
file_menu.add_command(label='复制', command=func)
file_menu.add_command(label='保存', command=func)

menu_btn.config(menu=file_menu)
win.mainloop()




