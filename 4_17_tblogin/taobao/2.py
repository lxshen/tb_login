from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://127.0.0.1:8080')
driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path='C:\\Users\\TuiQuan\\Desktop\\PycharmProjects\\4_17_tblogin\\chromedriver.exe')

driver.get('https://login.taobao.com/member/login.jhtml')
print(driver.title)
# 获取密码登陆
time.sleep(2)

element = driver.find_element_by_xpath('//*[@id="J_LoginBox"]/div[1]/div[1]')
element.click()



name = driver.find_element_by_xpath('//*[@id="TPL_username_1"]')

# webdriver.ActionChains(driver).move_to_element(name).perform()
# time.sleep(2)

# ActionChains(driver).move_by_offset(50,0).perform()
# time.sleep(0.5)
# ActionChains(driver).move_by_offset(155,155).perform()

name.send_keys("1")
time.sleep(0.5)
name.send_keys("5")
time.sleep(0.5)
name.send_keys("2")
time.sleep(0.5)
name.send_keys("0")
time.sleep(0.5)
name.send_keys("3")
time.sleep(0.5)
name.send_keys("8")
time.sleep(0.5)
name.send_keys("0")
time.sleep(0.5)
name.send_keys("4")
time.sleep(0.5)
name.send_keys("2")
time.sleep(0.5)
name.send_keys("7")
time.sleep(0.5)
name.send_keys("5")
time.sleep(0.5)
name.send_keys(Keys.TAB)

passwd = driver.find_element_by_xpath('//*[@id="TPL_password_1"]')
passwd.send_keys("t")
time.sleep(0.5)
passwd.send_keys("a")
time.sleep(0.5)
passwd.send_keys("o")
time.sleep(0.5)
passwd.send_keys("b")
time.sleep(0.5)
passwd.send_keys("a")
time.sleep(0.5)
passwd.send_keys("o")
time.sleep(0.5)
passwd.send_keys("m")
time.sleep(0.5)
passwd.send_keys("m")
time.sleep(0.5)
passwd.send_keys("2")
time.sleep(0.5)
passwd.send_keys("1")
time.sleep(0.5)
passwd.send_keys("/")
time.sleep(0.5)
passwd.send_keys("/")
time.sleep(0.5)

hk = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(driver).drag_and_drop_by_offset(hk,400,1).perform()

time.sleep(2)
text=driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
if text.text.startswith(u'请在下方'):
        print('成功滑动')

if text.text.startswith(u'请点击'):
    print('成功滑动')


name.send_keys(Keys.TAB)
sub = driver.find_element_by_xpath('//*[@id="J_SubmitStatic"]')
sub.click()


