# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 14:39
# @File :tkinter21
# @Project : GuideTest
from tkinter import ttk
import tkinter

win = tkinter.Tk()
win.title("Study")
win.geometry('400x250')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
win.resizable(False, False)

def func(event):
    text.insert('insert', cbox.get() + "\n")

cbox = ttk.Combobox(win)
cbox.grid(row=1, sticky="NW")
cbox['value'] = ('C', 'C#', 'Go', 'Python', 'Java')
cbox.current(3)
cbox.bind("<<ComboboxSelected>>", func)
text = tkinter.Text(win)
text.grid(pady=5)
win.mainloop()
