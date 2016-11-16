from selenium import webdriver

browser = webdriver.Chrome('/usr/lib64/chromium/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
