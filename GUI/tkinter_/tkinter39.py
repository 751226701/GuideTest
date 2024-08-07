# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 11:38
# @File :tkinter39
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.title("C语言中文网")
win.geometry('800x350+200+200')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

frame_left = tk.LabelFrame(win, text="教程", labelanchor="w", bg='#5CACEE')
frame_left.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.5)

label_1 = tk.Label(frame_left, text="C语言")
label_1.place(relx=0.2, rely=0.2)
label_2 = tk.Label(frame_left, text="Python")
label_2.place(relx=0.6, rely=0.2)
label_3 = tk.Label(frame_left, text="Java")
label_3.place(relx=0.2, rely=0.6)
label_4 = tk.Label(frame_left, text="C++")
label_4.place(relx=0.6, rely=0.6)
# 定义第二个容器，使用 labelanchor ='w' 来设置标题的方位
frame_right = tk.LabelFrame(win, text="辅导班", labelanchor="w", bg='#66CDAA')
# 使用 place 控制 LabelFrame 的位置
frame_right.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.6)
label_1 = tk.Label(frame_right, text="C语言辅导班")
label_1.place(relx=0.2, rely=0.2)
label_2 = tk.Label(frame_right, text="数据结构")
label_2.place(relx=0.6, rely=0.2)
label_3 = tk.Label(frame_right, text="C++辅导班")
label_3.place(relx=0.2, rely=0.6)
label_4 = tk.Label(frame_right, text="Python答疑")
label_4.place(relx=0.6, rely=0.6)

win.mainloop()
