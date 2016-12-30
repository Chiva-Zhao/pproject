from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.PhantomJS(executable_path='D:\\phantomjs211\\bin\\phantomjs.exe')
driver.get('https://rong.36kr.com/userinfo/252012')
data = driver.page_source
soup = BeautifulSoup(data, "html.parser")
content = soup.find_all('div', class_='content-detail user-profile')[0]
for row in content.find_all(attrs={"ng-include": "'templates/user/finacing.html'"}):
    for name in row.find_all(attrs={"ng-if":"user.invest_cases.length"}):
        a = name.find_all('div',class_='info-heading')[0].get_text()
        b = name.find_all('div',class_='intro')[0].get_text()
        c = row.find_all('div',class_='content')[0].get_text()
        print(a, b,c)
