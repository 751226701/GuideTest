# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 10:56
# @File :tkinter38
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.title("C语言中文网")
win.geometry('400x350+200+200')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

frame = tk.Frame(win)
frame.pack()

frame_left = tk.Frame(frame)
tk.Label(frame_left, text='左侧标签1', bg='green', width=10, height=5).grid(row=0, column=0)
tk.Label(frame_left, text='左侧标签2', bg='blue', width=10, height=5).grid(row=1, column=1)
frame_left.pack(side=tk.LEFT)

frame_right = tk.Frame(frame)
tk.Label(frame_right, text='右侧标签1', bg='gray', width=10, height=5).grid(row=0, column=1)
tk.Label(frame_right, text='右侧标签2', bg='pink', width=10, height=5).grid(row=1, column=0)
tk.Label(frame_right, text='右侧标签3', bg='purple', width=10, height=5).grid(row=1, column=1)
frame_right.pack(side=tk.RIGHT)
win.mainloop()
