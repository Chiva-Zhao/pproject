import re

import requests

base_url = "http://www.bjrbj.gov.cn/csibiz/home/static/catalogs/catalog_74200/74200.html"
response = requests.get(base_url)
content_pattern = re.compile(r'<td height="24">(.*?)</td>')
if response.status_code == 200:
    content = response.text.encode('utf8', 'ignore').decode('utf8', 'ignore')
    content = content.replace("\n", '')
result = re.findall(content_pattern, content)
for r in result:
    print(r)
