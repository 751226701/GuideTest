# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 14:26
# @File :tkinter42
# @Project : GuideTest
from tkinter import *
import tkinter.filedialog

def askfile():
    filename = tkinter.filedialog.askopenfilename()
    if filename != "":
        lb.config(text=filename)
    else:
        lb.config(text="您没有选择任何文件")

root = Tk()
root.title("C语言中文网")
root.geometry('400x200+300+300')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
btn = Button(root, text="选择文件", relief=RAISED, command=askfile)
btn.grid(row=0, column=0)
lb = Label(root, text='', bg='#87CEEB')
lb.grid(row=0, column=1, padx=5)

root.mainloop()
































