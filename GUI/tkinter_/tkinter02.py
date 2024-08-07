# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/1 19:17
# @File :tkinter02
# @Project : GuideTest

from tkinter import Tk
from tkinter import messagebox

root = Tk()

def QueryWindow():
    if messagebox.showwarning('警告', '出现了一个错误'):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', QueryWindow())
root.mainloop()
