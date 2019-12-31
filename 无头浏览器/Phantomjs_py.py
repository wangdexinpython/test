from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#
# def main():
#     # chrome_options = Options()
#     # chrome_options.add_argument('--headless')
#     # chrome_options.add_argument('--disable-gpu')
#     # driver = webdriver.Chrome(executable_path=r'D:\tools\chromedriver.exe', chrome_options=chrome_options)
#     # driver.get("https://www.baidu.com")
#     # print(driver.page_source)
#     path = r'D:\tools\chromedriver'
#     driver = webdriver.Chrome(executable_path=path)
#     driver.get("https://www.baidu.com")
#     print(driver.page_source)
#     driver.close()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=r'C:\Users\EDZ\Documents\WeChat Files\wodexinwolai\FileStorage\File\2019-05/chromedriver', chrome_options=chrome_options)
    driver.get("https://www.baidu.com")
    print(driver.page_source)
    driver.close()
if __name__ == '__main__':
    main()

