# 简单的时间转换，比如天到秒，小时到分钟等的转换
from datetime import timedelta, datetime

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days, c.seconds, c.seconds / 3600, c.total_seconds() / 3600)

a = datetime(2017, 4, 3)
b = datetime(2018, 5, 3)
print(a, a + timedelta(days=10))
print(b - a)
now = datetime.now()
print(now, now + timedelta(minutes=10))
# 在计算的时候，需要注意的是 datetime 会自动处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print((a - b).days)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)

a = datetime(2012, 9, 23)
# a + timedelta(months=1)  TypeError: 'months' is an invalid keyword argument for this function
from dateutil.relativedelta import relativedelta

print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))
# Time between two dates
b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d, d.days, d.months)
