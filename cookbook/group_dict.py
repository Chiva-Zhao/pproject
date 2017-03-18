# 通过某个字段将记录分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby
import pprint


def sort_group():
    rows.sort(key=itemgetter('date'))
    # pprint.pprint(rows)
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)


from collections import defaultdict


def random_group():
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)
    pprint.pprint(rows_by_date)

random_group()