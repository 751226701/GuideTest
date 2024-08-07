# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 13:03
# @File :tkinter16
# @Project : GuideTest
from tkinter import *

win = Tk()
win.title("Study")
# 创建一个Text控件
text = Text(win)
# 在Text控件内插入- -段文字 ，INSERT表示在光标处插入，END表示在末尾处插入
text.insert(INSERT, "C语言中文网（网址：c.biancheng.net），一个有温度的网站，一生只做一件事\n\n")
# 跳下一行
text.insert(INSERT, "\n\n")
# 在Text控件内插入- -个按钮
button = Button(text, text="关闭", command=win.quit)
text.window_create(END, window=button)
# 填充水平和垂直方向,这里设置 expand为 True 否则不能垂直方向延展
text.pack(fill=BOTH, expand=True)
# 在第一行文字的第0个字符到第6个字符处插入标签，标签名称为"name"
text.tag_add("name", "1.0", "1.6")
# 将插入的按钮设置其标签名为"button"
text.tag_add("button", button)
# 使用 tag_config() 来改变标签"name"的前景与背景颜色,并加下画线，通过标签控制字符的样式
text.tag_config("name", font=('微软雅黑', 18, 'bold'), background="yellow", foreground="blue", underline=1)
# 设置标签"button"的居中排列
text.tag_config("button", justify="center")
# 开始程序循环
win.mainloop()
