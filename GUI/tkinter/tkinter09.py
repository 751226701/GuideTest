# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/2 11:41
# @File :tkinter09
# @Project : GuideTest
import tkinter as tk
import time

root = tk.Tk()
root.title("Study")
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
root.geometry('500x180+180+150')
root.resizable(0, 0)
root.title("时钟")


def getTime():
    dstr.set(time.strftime("%H:%M:%S"))
    root.after(1000, getTime)


dstr = tk.StringVar()
lb = tk.Label(root, textvariable=dstr, fg='green', font=('微软雅黑', 85))
lb.pack()
getTime()
root.mainloop()
