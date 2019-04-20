from selenium import webdriver
import time


browser = webdriver.Chrome(executable_path='chromedriver')

browser.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
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
sub.click()

