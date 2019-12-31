#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# time: 2018/10/26 下午12:03
import asyncio
import time
# from fliggy.alifunc import input_time_random, mouse_slide
# from fliggy.exe_js import js5, js4, js3, js2, js1
from alifunc import input_time_random, mouse_slide
from exe_js import js5, js4, js3, js2, js1

from pyppeteer.launcher import launch, connect


async def fliggy_index_page():
    browser = await launch({'headless': False, 'appMode': True, 'args': ['--no-sandbox']})
    page = await browser.newPage()
    print(page)
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    # await page.goto('http://www.fliggy.com')
    # await page.screenshot({'path': './index.png'})
    await page.goto('http://www.fliggy.com')
    await page.goto(url='https://login.taobao.com/member/login.jhtml?spm=181.11358650.0.0.45502bd166imN6&f=top&redirectURL=https%3A%2F%2Fwww.alitrip.com%2F%3Fttid%3Dseo.000000574%26seoType%3Dorigin%26natue%3Dtrue&ttid=seo.000000574')

    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)

    username, pwd = '我的心我来', 'jiexin88'
    await page.click('.login-switch')

    # await page.click('.forget-pwd J_Quick2Static')


    await page.type('.J_UserName', username, {'delay': input_time_random() - 50})
    await page.type('#J_StandardPwd input', pwd, {'delay': input_time_random()})
    # await page.screenshot({'path': 'fliggy_longin.png'})

    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块
    print(slider)
    time.sleep(2)

    if slider:
        print('出现滑块情况判定')
        # await page.screenshot({'path': './headless-login-slide.png'})
        flag = await mouse_slide(page=page)
        print(flag)
        if flag:
            await get_cookie(page)
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
            else:
                print(page.url)
                await get_cookie(page)

        await page.type('#J_StandardPwd input', pwd, {'delay': input_time_random()})
        slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块
        print(slider)
        time.sleep(2)
        if slider:
            print('出现滑块情况判定')
            await page.screenshot({'path': './headless-login-slide.png'})
            flag = await mouse_slide(page=page)
            if flag:
                await get_cookie(page)






async def get_cookie(page):
    res = await page.content()
    cookies_list = await page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1}; '
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print(cookies)
    return cookies

asyncio.get_event_loop().run_until_complete(fliggy_index_page())
