# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 14:58
# @File :tkinter22
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.title("Study")
win.geometry('400x250')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

v = tk.IntVar()
v.set(1)

site = [("C语言中文网", 1),
        ("CSDN平台", 2),
        ("知乎平台", 3),
        ("知乎平台", 4)]


def select():
    dict = {1: 'C语言中文网', 2: '菜鸟教程', 3: 'W3SCHOOL', 4: '微学苑'}
    strings = '您选择了' + dict.get(v.get()) + '，祝您学习愉快'
    lable.config(text=strings)


lable = tk.Label(win, font=('微软雅黑', '15', 'bold'), fg='#43CD80')
lable.pack(side='bottom')

for name, value in site:
    tk.Radiobutton(win, text=name, variable=v, value=value, command=select, indicatoron=False).pack(anchor='w')

win.mainloop()
