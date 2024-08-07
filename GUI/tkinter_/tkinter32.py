# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 9:08
# @File :tkinter32
# @Project : GuideTest
from tkinter import *

# 定义事件函数，必须用event参数
def show_key(event):
    s = event.keysym
    lb.config(text=s)

root = Tk()
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('450x350+300+200')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

lb = Label(root, text="请按键", fg="blue", font=('微软雅黑',15))
lb.bind('<Key>', show_key)
lb.focus_set()
lb.pack()

root.mainloop()






























