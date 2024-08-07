# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 14:26
# @File :tkinter44
# @Project : GuideTest
import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("颜色选择")
root.geometry('400x200+300+300')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

def callback():
    colorvalue = tk.colorchooser.askcolor()
    lb.config(text="颜色值：" + str(colorvalue))

lb = tk.Label(root, text='', font=('宋体', 10))
lb.pack()
tk.Button(root, text="点击选择颜色", command=callback, width=10, bg='#9AC0CD').pack()

root.mainloop()





























