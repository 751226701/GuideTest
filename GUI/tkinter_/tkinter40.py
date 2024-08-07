# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 13:03
# @File :tkinter40
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.title("C语言中文网")
win.geometry('400x400+200+200')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

p_win = tk.PanedWindow(win)
p_win.pack(fill=tk.BOTH, expand=1)

left1 = tk.Label(p_win, text='C语言中文网', bg='#7CCD7C', width=10, font=('微软雅黑', 15))
p_win.add(left1)
left2 = tk.Label(p_win, text='网址：c.biancheng.net', bg='#9AC0CD', width=10, font=('微软雅黑', 15))
p_win.add(left2)

p_win2 = tk.PanedWindow(orient=tk.VERTICAL, showhandle=True, sashrelief="sunken")
p_win.add(p_win2)

top_label = tk.Label(p_win2, text='教程', bg='#7171C6', height=8, font=('宋体', 15))
p_win2.add(top_label)
bottom_label = tk.Label(p_win2, text='辅导班', bg='#8968CD', font=('宋体', 15))
p_win2.add(bottom_label)

win.mainloop()
