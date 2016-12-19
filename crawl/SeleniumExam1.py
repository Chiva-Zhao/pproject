from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path='D:\\phantomjs211\\bin\\phantomjs.exe')
driver.get('https://rong.36kr.com/userinfo/252012')
a = driver.find_element_by_class_name("user-name")
print(a.text)
