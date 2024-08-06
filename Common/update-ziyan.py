# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/5 8:45
# @File :debug.py
# @Project : ZS22A_UI
import os
from time import sleep
from datetime import datetime
from pywinauto import Desktop, Application
from playwright.sync_api import Playwright, sync_playwright, expect

"""获取当前时间"""
def get_time():
    return datetime.now().strftime("%Y%m%d-%H%M%S")
"""在当前路径下创建测试文件夹"""
def getTestPath(folder_name):
    current_path = os.getcwd()
    if not os.path.exists(os.path.join(current_path, folder_name)):
        os.makedirs(os.path.join(current_path, folder_name))
        return os.path.join(current_path, folder_name)
    else:
        return os.path.join(current_path, folder_name)

url = "http://192.168.21.23/#/login"
arm_path = r"C:\Users\gd09186\Desktop\ZS10F_V2.2.6.img"
asic_path = ""
app_path = ""
pic_path = getTestPath("TestPicture") + os.path.sep + get_time() + ".png"


def update_arm(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto(url)
    page.get_by_placeholder("请输入用户名").fill("admin")
    page.get_by_placeholder("请输入密码").fill("admin123")
    sleep(3)
    page.get_by_role("button", name="登录").click()
    page.get_by_text("系统管理").click()
    page.get_by_text("系统维护").click()
    page.get_by_role("menuitem", name="系统升级").click()
    page.get_by_role("button", name="选择").first.click()

    # 选择文件进行升级
    sleep(2)
    app = Application().connect(title_re="打开")
    dlg = app.window(title_re="打开")
    dlg['Edit'].type_keys(arm_path)
    dlg['Edit'].type_keys("{ENTER}")
    page.get_by_role("button", name="ARM固件升级").click()
    page.get_by_role("button", name="确认升级").click()
    expect(page.get_by_text("系统正在升级中，切勿关闭当前窗口以及切断电源……")).to_be_visible()
    print("设备升级中.......................")
    page.screenshot(path=pic_path)

    # 判断设备是否升级成功
    try:
        expect(page.get_by_text("设备重启中，请稍后！")).to_be_visible(timeout=300000)
        page.screenshot(path=pic_path)
        print("设备准备重启！")

        expect(page.get_by_text("系统升级成功！")).to_be_visible(timeout=300000)
        page.screenshot(path=pic_path)
        print("升级成功！")

    except TimeoutError as e:
        print("升级失败")
        raise e

if __name__ == '__main__':
    with sync_playwright() as playwright:
        update_arm(playwright)

