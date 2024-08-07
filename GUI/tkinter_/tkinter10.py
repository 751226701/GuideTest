# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 9:22
# @File :tkinter10
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.geometry('256x100')
win.title('Study')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
win.resizable(False, False)

entry1 = tk.Entry(win)
entry1.pack(padx=20, pady=20)
entry1.delete(0, "end")
entry1.insert(0, "C语言中文网，网址：c.biancheng.net")
print(entry1.get())
# entry1.delete(0, tk.END)
win.mainloop()



