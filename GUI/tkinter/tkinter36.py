# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 10:04
# @File :tkinter36
# @Project : GuideTest
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("C语言中文网")
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
root.resizable(False, False)

tk.Label(root, text="用户名：").grid(row=0, sticky="w")
tk.Label(root, text="密码：").grid(row=1, sticky="w")

tk.Entry(root).grid(row=0, column=1)
tk.Entry(root, show="*").grid(row=1, column=1)

photo = tk.PhotoImage(file=r"C:\Users\gd09186\Pictures\Camera Roll\悟空.gif")
tk.Label(root, image=photo).grid(row=0, column=2, rowspan=2, padx='4px', pady='5px')

def login():
    messagebox.showinfo('欢迎来到C语言中文网')

tk.Button(root, text="登录", width=10, command=login).grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)
tk.Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, columnspan=2, sticky="e", padx=10, pady=5)
root.mainloop()





















