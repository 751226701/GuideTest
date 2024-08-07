# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 15:39
# @File :tkinter23
# @Project : GuideTest
from tkinter import *

win = Tk()
win.title("Study")
win.geometry('500x200')
win.resizable(False, False)
lb = Label(text='C语言中文网答疑辅导班', font=('微软雅黑', 18, 'bold'), fg='#CD7054')
lb.pack()
win.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")

checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()

check1 = Checkbutton(win, text="Python", font=('微软雅黑', 15, 'bold'), variable=checkVar1, onvalue=1, offvalue=0)
check2 = Checkbutton(win, text="C语言", font=('微软雅黑', 15, 'bold'), variable=checkVar2, onvalue=1, offvalue=0)
check3 = Checkbutton(win, text="JAVA", font=('微软雅黑', 15, 'bold'), variable=checkVar3, onvalue=1, offvalue=0)
check1.select()

check1.pack(side=LEFT)
check2.pack(side=LEFT)
check3.pack(side=LEFT)

def study():
    if checkVar1.get() == 0 and checkVar2.get() == 0 and checkVar3.get() == 0:
        s = '您还没选择任语言'
    else:
        s1 = "Python" if checkVar1.get() == 1 else ""
        s2 = "C语言" if checkVar2.get() == 1 else ""
        s3 = "Java" if checkVar3.get() == 1 else ""
        s = "您选择了%s %s %s" % (s1, s2, s3)
        # 设置标签lb2的字体
    lb2.config(text=s)

btn = Button(win, text="选好了", bg='#BEBEBE', command=study)
btn.pack(side=LEFT)
# 该标签，用来显示选择的文本
lb2 = Label(win, text='', bg='#9BCD9B', font=('微软雅黑', 11, 'bold'), width=5, height=2)
lb2.pack(side=BOTTOM, fill=X)
win.mainloop()
