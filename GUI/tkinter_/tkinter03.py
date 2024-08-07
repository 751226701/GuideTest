# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/1 19:24
# @File :tkinter03
# @Project : GuideTest
import tkinter as tk


def callback():
    print("执行回调函数")


window = tk.Tk()
window.title('Study')
width = 300
height = 300
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
button = tk.Button(window, text="执行", command=callback)
button.pack()
window.mainloop()
