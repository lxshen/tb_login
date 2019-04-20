# -*-coding: utf-8 -*-
import webbrowser as web
import webbrowser
import time
chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'            #  例如我的：C:\***\***\***\***\Google\Chrome\Application\chrome.exe
a = web.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
browser = web.get('chrome').open_new_tab('https://login.taobao.com/member/login.jhtml')

print(browser.title)
# 获取密码登陆
time.sleep(2)
element = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a')
element.click()
time.sleep(2)
name = browser.find_element_by_xpath('//*[@id="loginname"]')
name.send_keys("15203804275")
time.sleep(2)
passwd = browser.find_element_by_xpath('//*[@id="nloginpwd"]')
passwd.send_keys("jingdongmm21//")
# 获取登陆按钮
sub = browser.find_element_by_xpath('//*[@id="loginsubmit"]')
