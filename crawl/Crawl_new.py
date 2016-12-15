import json
import urllib.request

url = 'https://rong.36kr.com/api/organization/investor?page='
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
data = response.read()
data = data.decode()
# 处理data的中文
myjson = json.loads(data)  # data的type必须为str.
print(myjson)
print(myjson['data']['data'][0]['user']['name'])
