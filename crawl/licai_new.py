from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs')
# driver.get('http://www.licai.com/simu/gongsi.html')
# with open("gssmzquanbu1.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
# csvwriter = csv.writer(datacsv, dialect=("excel"))
driver = webdriver.PhantomJS(
    executable_path=r'D:\\phantomjs211\\bin\\phantomjs.exe')
driver.get('http://www.licai.com/simu/gongsi.html')
old_scroll_height = 0
js1 = 'return document.body.scrollHeight'
js2 = 'window.scrollTo(0, document.body.scrollHeight)'
while (driver.execute_script(js1) >= old_scroll_height):
    old_scroll_height = driver.execute_script(js1)
    print(old_scroll_height)
    driver.execute_script(js2)
    time.sleep(3)
data = driver.page_source
soup = BeautifulSoup(data, "html.parser")
list1 = soup.find(id="tablist")
rows = list1.find_all("tr")
print(len(rows))
# for tr in rows:
#     try:
#         tds = tr.find_all('td')
#         gs = tds[1].get_text()
#         wz = tds[1].find('a').attrs['href']
#         cl = tds[2].get_text()
#         name = tds[3].get_text()
#     except:
#         tds = ''
#         gs = ''
#         wz = ''
#         cl = ''
#         name = ''
#     if tds == '' or gs == '' or wz == '' or cl == '' or name == '':
#         continue
#     print(gs, wz, cl)
# csvwriter.writerow([gs,wz,cl,name])
