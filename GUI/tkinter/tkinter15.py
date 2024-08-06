# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 11:35
# @File :tkinter15
# @Project : GuideTest

from tkinter import *

root = Tk()
root.title("Study")
root.geometry('400x200')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
text = Text(root, width=35, height=15)
text.pack()
text.insert(INSERT, "hello world")
text.insert("insert", "i love python")
print(text.get("1.3", "1.end"))
root.mainloop()



