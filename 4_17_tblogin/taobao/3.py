# -*-coding: utf-8 -*-

import time
import asyncio
from pyppeteer import launch
from taobao.raoguo.exe_js import js1, js2, js3, js4, js5
import random
from taobao.raoguo.alifunc import mouse_slide

async def main():
    # headless = True
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': 1800, 'height': 1000})
    await page.goto('https://login.taobao.com')

    await page.evaluate(js1)
    # await page.evaluate(js2)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)
    # 点击密码登录
    await page.click('.login-switch')

    await page.type('#TPL_username_1', '15203804275',{'delay': 200} )
    await page.type('#TPL_password_1', 'taobaomm21//',{'delay': 200} )
    # 点击搜索按钮
    time.sleep(2)


    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块

    if slider:
        print('出现滑块情况判定')
        try:
            await page.screenshot({'path': './headless-login-slide.png'})
            flag = await mouse_slide(page=page)
            print('flag')
            if flag:
                print(1)
                # await page.click('#J_SubmitStatic')
                await get_cookie(page)
        except:
            print('cuowu')

    else:
        await page.keyboard.press('Enter')
        await page.waitFor(20)
        await page.waitForNavigation()
        try:
            global error
            error = await page.Jeval('.error', 'node => node.textContent')
        except Exception as e:
            error = None
        finally:
            if error:
                print('确保账户安全重新入输入')
                # 程序退出。
                loop.close()
            else:
                print(page.url)
                await get_cookie(page)

    # await page.hover('#nc_1_n1z')
    # await page.mouse.down()
    # await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
    # time.sleep(2)
    # await page.mouse.up()
    # await page.click('#J_SubmitStatic')
    # time.sleep(10)

# 获取登录后cookie
async def get_cookie(page):
    res = await page.content()
    cookies_list = await page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1};'
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print(cookies)
    return cookies

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())