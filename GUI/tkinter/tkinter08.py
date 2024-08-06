# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/2 11:03
# @File :tkinter08
# @Project : GuideTest
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Study")
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
win.geometry('400x300+100+100')
win.resizable(False, False)
tk.Label(win, text="账号：").grid(row=0)
tk.Label(win, text="密码：").grid(row=1)

e1 = tk.Entry(win)
e2 = tk.Entry(win, show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def login():
    messagebox.showinfo("提示", "登录成功！")
tk.Button(win, text="登录", width=10, command=login).grid(row=3, column=0, stick="w", padx=10, pady=5)
tk.Button(win, text="退出", width=10, command=win.quit).grid(row=3, column=1, stick="e", padx=10, pady=5)
win.mainloop()

