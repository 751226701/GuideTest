# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/2 8:48
# @File :tkinter04
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.title("title")
win.geometry('400x300')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
label = tk.Label(win, text="Study", font=('宋体', 20, 'bold italic'), bg="#7CCD7C",
                 # 设置标签内容区大小
                 width=30, height=20,
                 # 设置填充区距离、边框宽度和其样式（凹陷式）
                 padx=10, pady=15, borderwidth=10, relief="sunken")
label.pack()
win.mainloop()






