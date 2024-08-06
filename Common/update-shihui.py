# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/7/4 14:22
# @File :update-shihui.py
# @Project : GuideTest
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

url = "http://192.168.21.213/"
arm_path = r"C:\Users\gd09186\Desktop\ZS10D.bin"
pic_path = getTestPath("TestPicture") + os.path.sep + get_time() + ".png"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("http://192.168.21.213/")
    page.get_by_placeholder("用户名").fill("admin")
    page.get_by_placeholder("密码").fill("admin")
    sleep(3)
    page.get_by_role("link", name="登录").click()
    page.get_by_role("link", name="设置").click()
    page.locator("a").filter(has_text="系统管理").click()
    page.get_by_text("系统维护").click()
    page.get_by_text("固件升级").click()
    page.locator(".fn-left.fn-relative").click()
    sleep(2)

    app = Application().connect(title_re="打开")
    dlg = app.window(title_re="打开")
    dlg['Edit'].type_keys(arm_path)
    dlg['Edit'].type_keys("{ENTER}")
    page.locator("#upg_update").click()
    if not page.get_by_text("正在传输文件，请勿离开该页面或关闭浏览器……").is_visible():
        page.locator("#upg_update").click()
    expect(page.get_by_text("正在传输文件，请勿离开该页面或关闭浏览器……")).to_be_visible()
    print("设备升级中.............")
    expect(page.get_by_text("设备重启中，请稍候……")).to_be_visible(timeout=300000)
    print("升级成功！")
    sleep(30)
    page.screenshot(path=pic_path)



    # ---------------------
    context.close()
    browser.close()

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)

