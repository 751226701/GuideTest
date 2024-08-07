# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 9:42
# @File :tkinter11
# @Project : GuideTest
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry('250x200+250+200')
win.title('Study')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
win.resizable(False, False)


def check():
    if entry1.get() == "C语言中文网":
        messagebox.showinfo("提示", "输入正确")
        return True
    else:
        messagebox.showinfo("提示", "输入错误")
        entry1.delete(0, tk.END)
        return False


lab1 = tk.Label(win, text="账号：")
lab2 = tk.Label(win, text="密码：")
lab1.grid(row=0)
lab2.grid(row=1)

dstr = tk.StringVar()
entry1 = tk.Entry(win, textvariable=dstr, validate="focusout", validatecommand=check)
entry2 = tk.Entry(win)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

win.mainloop()



