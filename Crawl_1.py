import requests
import csv

from bs4 import BeautifulSoup

htm = 'http://www.cyzone.cn/f/20161126/2725.html'
res = requests.get(htm)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('p').st)
# for news in soup.select('p'):
for news in soup.select('.project-info'):
    for new in news.select('p'):
        h = news.get_text()
for inv in soup.select('.invest'):
    h1 = inv.get_text()
for name in soup.select('.people-info-intro'):
    h2 = name.get_text()
for rec in soup.select('.record'):
    h3 = rec.get_text()
print(h, h1, h2, h3)
with open("test.csv", "w", newline="") as datacsv:
    # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
    csvwriter.writerow([h,h1,h2,h3])