# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/2 10:40
# @File :tkinter07
# @Project : GuideTest

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Study")
window.geometry('400x300+300+200')


def callback():
    # 使用消息对话框控件，showinfo()表示温馨提示
    messagebox.showinfo(title="温馨提示", message="欢迎光临！")

im = tk.PhotoImage(r"C:\Users\gd09186\Pictures\Camera Roll\logo.gif")
tk.Button(window, text="button", bg='#7CCD7C', width=20, height=5, command=callback).pack()
window.mainloop()
