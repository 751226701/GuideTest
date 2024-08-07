# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 9:30
# @File :tkiinter11
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.geometry('256x100')
win.title('Study')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
win.resizable(False, False)

label1 = tk.Label(win, text="账号：")
label2 = tk.Label(win, text="密码：")

label1.grid(row=0)
label2.grid(row=1)

entry1 = tk.Entry(win)
entry2 = tk.Entry(win)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

win.mainloop()



