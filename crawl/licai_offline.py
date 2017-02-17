import requests
from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver

with open("gssmzquanbu3.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    fb = open(r'C:\Users\Administrator\Desktop\888.txt')
    alldata = fb.read().split("\n")
    for i in range(len(alldata)):
        data = alldata[i].split("\t")
        a1 = data[0]
        a2 = data[1]
        b1 = data[2]
        url = 'http://www.licai.com/' + b1
        html = requests.get(url)
        time.sleep(3)
        html.encoding = 'gbk'
        soup = BeautifulSoup(html.text, "html.parser")

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
            list1 = soup.find_all(id="jj1")

            if list1.find_all('div', class_='cont c01') and list1.find_all:
                print('list1 hello')

                for rw in list1.find_all('div', class_='cont c01'):
                    try:
                        y = ''
                        for nm in rw.find_all('p'):
                            y += nm.get_text() + ','
                    except:
                        y = ''
                    if y == '':
                        continue
            else:
                continue;
        except:
            continue;

        try:
            list2 = soup.find(id="jj2")

            if list2 and list2.find_all('div', class_='cont c02') and list2.find_all:
                print('list2 hello')

                for rw in list2.find_all('div', class_='cont c02'):
                    try:
                        d = ''
                        for nm in rw.find_all('p'):
                            d += nm.get_text() + ','
                    except:
                        d = ''
                    if d == '':
                        continue
            else:
                continue;
        except:
            continue;
        try:
            list3 = soup.find(id="jj3")
            if list3 and list3.find_all('div', class_='cont c03') and list3.find_all:
                print('list3 hello')
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
                if list4.find_all('div', class_='cont c04') and list4.find_all:
                    print('list4 hello')
                else:
                    pass
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
                    csvwriter.writerow([a1, a2, a, b, c, e, f, h, y, d, x, q])
        except:
            continue