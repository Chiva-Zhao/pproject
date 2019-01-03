import requests
from bs4 import BeautifulSoup
import time

url = "http://www.stats.gov.cn/tjsj/tjbz/tjypflml/"

time.sleep(1)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
html = requests.get(url=url, headers=headers)
html.encoding = 'utf-8'
bsobj = BeautifulSoup(html.text,'html.parser')
rows = bsobj.findAll("span", {"class": "cont_tit"})
for each in rows:
    # print(each)
    print(each.find("font").text)