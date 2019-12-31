import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://passport.fang.com/?backurl=http://yt.fang.com/?s=BDPZ-BL')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())





# <a href="" class="forget-pwd J_Quick2Static" target="_blank" data-spm-anchor-id="a2107.1.0.0">密码登录</a>