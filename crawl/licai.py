from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import requests

with open("gssmz.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    driver = webdriver.PhantomJS(
        executable_path=r'D:\\phantomjs211\\bin\\phantomjs.exe')
    driver.get('http://www.licai.com/simu/jingli.html')
    for i in range(19):
        driver.execute_script("window.scrollBy(0," + str(i * 1000 + 2000) + ")")
        # time.sleep(3)
        if i == 18:
            count = 0
            data = driver.page_source
            soup = BeautifulSoup(data, "html.parser")
            list = soup.find(id="list")
            rows = list.find_all("tr")
            print(len(rows))
            for tr in rows:
                tds = tr.find_all('td')
                a1 = tds[1].get_text()
                b1 = tds[1].find('a').attrs['href']
                # time.sleep(3)
                driver.get('http://www.licai.com/' + b1)
                data = driver.page_source
                soup = BeautifulSoup(data, "html.parser")
                for yy in soup.find_all('div', class_='detail l'):
                    for xx in yy.find_all('tbody'):
                        try:
                            wh = xx.find_all('tr')[0]
                            a = wh.find_all('td')[0].get_text().strip()
                            e = wh.find_all('td')[1].get_text().strip()
                            wh1 = xx.find_all('tr')[1]
                            b = wh1.find_all('td')[0].get_text().strip()
                            f = wh1.find_all('td')[1].get_text().strip()
                            wh2 = xx.find_all('tr')[2]
                            c = wh2.find_all('td')[0].get_text().strip()
                            h = wh2.find_all('td')[1].get_text().strip()
                        except:
                            wh = ''
                            a = ''
                            e = ''
                            wh1 = ''
                            b = ''
                            f = ''
                            wh2 = ''
                            c = ''
                            h = ''
                    if a == '' or b == '' or f == '' or c == '' or h == '' or e == '':
                        continue
                try:
                    list1 = soup.find(id="jj1")
                except:
                    list1 = ''
                if list1 == '':
                    continue
                # if list1.find_all('div', class_='cont c01') and list1.find_all:
                #     print('list1 hello')
                # else:
                #     pass
                for rw in list1.find_all('div', class_='cont c01'):
                    try:
                        y = ''
                        for nm in rw.find_all('p'):
                            y += nm.get_text() + ','
                    except:
                        y = ''
                    if y == '':
                        continue
                try:
                    list2 = soup.find(id="jj2")
                except:
                    list2 = ''
                if list2 == '':
                    continue
                # if list2.find_all('div', class_='cont c02') and list2.find_all:
                #     print('list2 hello')
                # else:
                #     pass
                for rw in list2.find_all('div', class_='cont c02'):
                    try:
                        d = ''
                        for nm in rw.find_all('p'):
                            d += nm.get_text() + ','
                    except:
                        d = ''
                    if d == '':
                        continue
                try:
                    list3 = soup.find(id="jj3")
                    if list3 and list3.find_all('div', class_='cont c03') and list3.find_all:
                        # print('list3 hello')
                        for rw in list3.find_all('div', class_='cont c03'):
                            try:
                                x = ''
                                for nm in rw.find_all('p'):
                                    x += nm.get_text() + ','
                            except:
                                x = ''
                            if x == '':
                                continue
                    else:
                        continue;
                except:
                    continue;
                try:
                    list4 = soup.find(id="jj4")
                    if list4:
                        # if list4.find_all('div', class_='cont c04') and list4.find_all:
                        #     print('list4 hello')
                        # else:
                        #     pass
                        for nm in list4.find_all('div', class_='cont c04'):
                            try:
                                q = ''
                                for nm in rw.find_all('p'):
                                    q += nm.get_text() + ','
                            except:
                                q = ''
                            if q == '':
                                continue
                            # print('写入' + str(i) + a1, a, b, c, e, f, h, y, d, x, q)
                            print('写入' + str(i) + a1)
                            # csvwriter.writerow([a1, a, b, c, e, f, h, y, d, x, q])
                except:
                    continue
