# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 9:25
# @File :tkinter33
# @Project : GuideTest
from tkinter import *


def handleMotion(event):
    lb1['text'] = '你移动了光标的所在位置'
    lb2['text'] = '目前光标位置：x =' + str(event.x) + ';y=' + str(event.y)
    print('光标当前位置', event.x, event.y)

win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

frame = Frame(win, relief=RAISED, borderwidth=2, width=300, height=200)
frame.bind('<Motion>', handleMotion)
lb1 = Label(frame, text='没有任何事件触发', bg='purple', )
lb1.place(x=20, y=20)
lb2 = Label(frame, text='')
lb2.place(x=16, y=60)
frame.pack(side=TOP)

win.mainloop()








