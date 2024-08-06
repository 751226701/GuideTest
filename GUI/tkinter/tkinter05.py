# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/2 9:24
# @File :tkinter05
# @Project : GuideTest
import tkinter as tk

win = tk.Tk()
win.title("title")
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
photo = tk.PhotoImage(file=r"C:\Users\gd09186\Pictures\Camera Roll\悟空.gif")
print(type(photo))
tk.Label(win, image=photo).pack(side="right")
tk.Label(win, text="Study", fg='#7CCD7C', font=('微软雅黑', 15, 'italic'), justify="left", padx=10).pack(side="left")
win.mainloop()
