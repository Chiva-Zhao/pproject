import json
import urllib.request
import types
import pandas as pd
from pandas import Series, DataFrame
from pandas.io.json import json_normalize

url = 'https://rong.36kr.com/api/organization/investor?page='
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
data = response.read()
data = data.decode()
myjson = json.loads(data)
print(myjson)
# users = myjson['data']['data'][0]['user']
users = json_normalize(myjson['data']['data'])
invest = json_normalize(myjson['data']['data'][0]['investCom'])
# siblings = DataFrame(users,columns=['name','intro'])
# print(users['user.name'])
# print(users['user.intro'])
df = DataFrame(users, columns=['user.name', 'user.intro'])
df2 = DataFrame(invest,columns=['brief','fundId','industry','name']);
print(df2)
