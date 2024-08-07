# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 10:09
# @File :tkinter13
# @Project : GuideTest
import tkinter as tk

root = tk.Tk()
root.title("Study")
root.geometry('300x200+300+300')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
# 如果是数字使用 from_和to参数，范围 0-20,并且与2步长递增或递减
w = tk.Spinbox(root, from_=0, to=20, increment=2, width=15, bg='#9BCD9B')
# 使用 values 参数以元组的形式进行传参
strings = tk.Spinbox(root, values=('Python', 'java', 'C语言', 'PHP'))
w.pack()
strings.pack()
root.mainloop()
