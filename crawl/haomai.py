from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

with open("hmjll3.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    driver = webdriver.PhantomJS(
        executable_path=r'C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs')

    driver.get('https://simu.howbuy.com/manager/')
    page = 0;
    while page < 3066:
        data = driver.page_source
        soup = BeautifulSoup(data, "html.parser")
        funlist = soup.find_all('div', class_='fund_list')
        list1 = funlist[0].find_all('tr')
        for tr in list1:
            try:
                tds = tr.find_all('td')
                a1 = tds[2].get_text()
                b1 = tds[2].find('a').attrs['href']
                a2 = tds[3].get_text()
                a4 = tds[4].get_text()
                a3 = tds[5].get_text()
            except:
                list1 = ''
                tds = ''
                a1 = ''
                a2 = ''
                a3 = ''
                a4 = ''
                b1 = ''
            if a1 == '' or a2 == '' or a3 == '' or a4 == '' or tds == '' or b1 == '':
                continue
            print(a1, a2, a3, a4, b1)
        # csvwriter.writerow([a1,a2,a3,a4,b1])
        driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()  # selenium的xpath用法，找到包含“下一页”的a标签去点击
        page = page + 1
        print(page)
        time.sleep(3)  #
