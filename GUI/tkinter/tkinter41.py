# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 13:34
# @File :tkinter41
# @Project : GuideTest
import tkinter as tk

root = tk.Tk()
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('400x350+300+300')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

def create_toplevel():
    top = tk.Toplevel()
    top.title("C语言中文网")
    top.geometry('300x200+100+100')
    top.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
    # 多行文本显示Message控件
    msg = tk.Label(top, text="网址：c.biancheng.net", bg='#9BCD9B', font=('宋体', 15))
    msg.pack()

tk.Button(root, text="点击创建Toplevel组件", width=20,height=3,command=create_toplevel).pack()
root.mainloop()



























