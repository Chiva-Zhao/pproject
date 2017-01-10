import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.cyzone.cn/d/20110626/9.html'
html = requests.get(url)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, "html.parser")
# print(soup)
ps = soup.findAll("p", class_='name')

for p in ps:
    print(p.getText())
    print(p.find('a')['href'])
