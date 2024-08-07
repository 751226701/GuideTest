# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 15:31
# @File :tkinter45
# @Project : GuideTest
from tkinter import *
from time import strftime

root = Tk()
root.geometry('500x300+300+300')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
root.title("Study")

lb = Label(root, font=("微软雅黑", 50, 'bold'), bg="#87CEEB", fg="#B452CD")
lb.pack(anchor=CENTER, fill=BOTH, expand=True)

mode = 'time'
def showtime():
    if mode == 'time':
        string = strftime("%H:%M:%S %p")
    else:
        string = strftime("%Y-%m-%d")
    lb.config(text=string)
    lb.after(1000, showtime)

def mouseClick(event):
    global mode
    if mode == 'time':
        mode = 'date'
    else:
        mode = 'time'

lb.bind("<Button>", mouseClick)
showtime()
root.mainloop()
































