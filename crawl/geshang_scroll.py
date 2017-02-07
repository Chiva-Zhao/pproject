from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import requests

driver = webdriver.PhantomJS(executable_path=r'D:\\phantomjs211\\bin\\phantomjs.exe')
driver.get('http://www.licai.com/simu/jingli.html')
for i in range(1, 19):
    driver.execute_script("window.scrollBy(0," + str(i * 1000 + 2000) + ")")
    time.sleep(3)
    if i == 18:
        data = driver.page_source
        soup = BeautifulSoup(data, "html.parser")
        print('新的页面\n')
        list = soup.find(id="list")
        for tr in list.find_all("tr"):
            tds = tr.find_all('td')
            a = tds[1].get_text()
            b = tds[1].find('a').attrs['href']
            print(a, b)
