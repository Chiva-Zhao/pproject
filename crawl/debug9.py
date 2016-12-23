import requests
from bs4 import BeautifulSoup
import csv
import time

with open("红杉0.csv", "w+", newline="\n", encoding="utf-8") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    for i in range(39):
        url = 'http://www.cyzone.cn/company/case-11-0-0-' + str(i) + '/'
        time.sleep(1)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        html = requests.get(url=url, headers=headers)
        # htm2 = urllib.request.urlopen(html)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, "html.parser")
        # for row in soup.find_all('tr', class_='table-plate3'):
        # a = row.find('span',class_='tp2_com').get_text()
        # b = row.find('div', class_='money').get_text()
        # c = row.find('td',class_= 'tp3').get_text()
        for row in soup.find_all('tr', class_='table-plate3'):
            # for rows in row.find_all('td'):
            w = ''
            a = row.find_all('td')[1].get_text()
            c = row.find_all('td')[9].get_text()
            d = row.find_all('td')[10].get_text()
            e = row.find_all('td')[-1].get_text()
            w = a + ', ' + c + ',' + d + ',' + e
            print('写入->' + str(i) + w.replace('\n', ''))
            csvwriter.writerow([w])
