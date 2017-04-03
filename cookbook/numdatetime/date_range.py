# 计算当前月份的日期范围
from datetime import date, datetime, timedelta
import calendar


# 接受任意 datetime 对象并返回一个由当前月份开始日和下个月开始日组成的元组对象
def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    print(days_in_month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


print(get_month_range())
a_day = timedelta(days=1)
first_day, last_day = get_month_range()
# 有了这个就可以很容易的在返回的日期范围上面做循环操作了
# while first_day < last_day:
#     print(first_day)
#     first_day += a_day


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1),
                    timedelta(hours=6)):
    print(d)
