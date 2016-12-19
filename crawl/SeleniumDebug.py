from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path='D:\\phantomjs211\\bin\\phantomjs.exe')
driver.get('http://www.cyzone.cn/r/20160926/44237.html')
content= driver.find_elements_by_class_name("content")
for con in content:
    print(con.text)