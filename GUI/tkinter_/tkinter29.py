# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/5 19:29
# @File :tkinter29
# @Project : GuideTest
import tkinter as tk

root = tk.Tk()
root.config(bg='#8DB6CD')
root.title("C语言中文网")
root.geometry('400x300')
root.iconbitmap(r"C:\Users\gd09186\Pictures\Camera Roll\悟空.ico")
def func():
    print("您通过弹出菜单执行了命令")

menu = tk.Menu(root, tearoff=False)
menu.add_command(label="新建", command=func)
menu.add_command(label="复制", command=func)
menu.add_command(label="粘贴", command=func)
menu.add_command(label="剪切", command=func)

def command(event):
    # 使用 post()在指定的位置显示弹出菜单
    menu.post(event.x_root, event.y_root)

# 绑定鼠标右键，这是鼠标绑定事件
# <Button-3>表示点击鼠标的右键，1 表示左键，2表示点击中间的滑轮
root.bind("<Button-3>", command)
root.mainloop()



