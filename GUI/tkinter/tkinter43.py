# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 14:26
# @File :tkinter43
# @Project : GuideTest
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def open_img():
    try:
        global img
        filepath = filedialog.askopenfilename()  # 打开文件，返回该文件的完整路径
        filename.set(filepath)
        img = Image.open(filename.get())
    except Exception as e:
        print("您没有选择任何文件", e)

def save_png():
    try:
        filetypes = [("PNG", "*.png"), ("JPG", "*.jpg"), ("GIF", "*.gif"), ("txt files", "*.txt"), ('All files', '*')]
        # 返回一个 pathname 文件路径字符串，如果取消或者关闭则返回空字符，返回文件如何操作是后续代码的事情，
        # 该函数知识返回选择文件的文件名字，不具备保存文件的能力
        filenewpath = filedialog.asksaveasfilename(title='保存文件',
                                                   filetypes=filetypes,
                                                   defaultextension='.png',
                                                   initialdir='C:/Users/Administrator/Desktop')
        path_var.set(filenewpath)
        # 保存文件
        img.save(str(path_var.get()))
    except Exception as e:
        print(e)

window = tk.Tk()
window.title("C语言中文网")
window.geometry('400x200+300+300')
window.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
filename = tk.StringVar()
path_var = tk.StringVar()
# 定义读取文件的组件
entry = tk.Entry(window, textvariable=filename)
entry.grid(row=1, column=0, padx=5, pady=5)
tk.Button(window, text='选择文件', command=open_img).grid(row=1, column=1, padx=5, pady=5)
# 定义保存文件的组件
entry1 = tk.Entry(window, textvariable=path_var)
entry1.grid(row=2, column=0, padx=5, pady=5)
tk.Button(window, text='保存文件', command=save_png).grid(row=2, column=1, padx=5, pady=5)
window.mainloop()
