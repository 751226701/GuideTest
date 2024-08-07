# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 16:41
# @File :tkinter26
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.title("购物界面")
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
win.geometry('450x200+450+250')
win.resizable(False, False)
label = tk.Label(win, bg='#9FB6CD', width=18, text='')
label.grid(row=2)

def select_price(value):
    label.config(text='您购买的数量是：' + value)

scale = tk.Scale(win, label="选择您要购买的数量", from_=1, to=100, orient=tk.HORIZONTAL, length=400,
                 tickinterval=9, command=select_price)

scale.grid(row=1)
win.mainloop()
