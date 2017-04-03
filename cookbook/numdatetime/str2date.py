# 字符窜转换为日期
from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
print(y, z - y)
print(datetime.strftime(z, '%A %B %d, %Y'))
