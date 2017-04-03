# 结合时区的日期操作
from datetime import datetime, timedelta
from pytz import timezone, utc, country_timezones

d = datetime(2012, 12, 21, 9, 30, 0)
# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
# 一旦日期被本地化了，它就可以转换为其他时区的时间了。为了得到班加罗尔对应的时间，你可以这样做
# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print('WRONG', later)
# 结果错误是因为它并没有考虑在本地时间中有一小时的跳跃。为了修正这个错误，
# 可以使用时区对象 normalize() 方法
later = central.normalize(loc_d + timedelta(minutes=30))
print('CORRECT', later)

# 处理本地化日期的通常的策略先将所有日期
# 转换为 UTC 时间，并用它来执行所有的中间存储和操作
print(loc_d)
utc_d = loc_d.astimezone(utc)
print(utc_d)
# 一旦转换为 UTC，你就不用去担心跟夏令时相关的问题了。因此，你可以跟之前
# 一样放心的执行常见的日期计算。当你想将输出变为本地时间的时候，使用合适的时
# 区去转换下就行了
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

# 当涉及到时区操作的时候，有个问题就是我们如何得到时区的名称。比如，在这个
# 例子中，我们如何知道“Asia/Kolkata”就是印度对应的时区名呢？为了查找，可以使
# 用 ISO 3166 国家代码作为关键字去查阅字典 pytz.country timezones
print(country_timezones('IN'),country_timezones('CN'))
