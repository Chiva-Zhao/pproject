# python -m http.server on some folder
import itertools
from pprint import pprint

my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'xxxx'}
print(my_dict)
pprint(my_dict)
# cat file.json | python -m json.tool
# python -m cProfile my_script.py #cProfile是⼀个⽐profile更快的实现， 因为它是⽤c写的
# CSV转换为json
# python -c "import csv,json;print(json.dumps(list(csv.reader(open('csv_file.csv')))))"
# 列表辗平
a_list = [[1, 2], [3, 4], [5, 6]]
print(a_list)
print(*a_list)
print(list(itertools.chain.from_iterable(a_list)))
print(list(itertools.chain(*a_list)))

import io

with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()
if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'
with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))