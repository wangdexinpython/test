from selenium import webdriver
path = r'/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=path)
def search():
    driver.get('https://www.google.com')
    response = driver.page_source
    print(response)
if __name__ == '__main__':
    total = search()