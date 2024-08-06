# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 13:39
# @File :tkinter18
# @Project : GuideTest
from tkinter import *

win = Tk()
win.title("Study")
win.geometry('400x200')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
listbox1 = Listbox(win)
listbox1.pack()
# i表示索引值，item 表示值，根据索引值的位置依次插入
for i, item in enumerate(["C", "C++", "C#", "Python", "Java"]):
    listbox1.insert(i, item)
# i表示索引值，item 表示值，根据索引值的位置依次插入
# for item in ["C", "C++", "C#", "Python", "Java"]:
#     listbox1.insert("end", item)
win.mainloop()
