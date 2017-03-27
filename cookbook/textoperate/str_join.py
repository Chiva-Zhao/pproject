# 合并拼接字符串
# 如果你想要合并的字符串是在一个序列或者 iterable 中，那么最快的方式就是使用 join() 方法\
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
data = ['ACME', 50, 91.1]


def use_join():
    print(' '.join(parts), ','.join(parts), ''.join(parts))
    a = 'Is Chicago'
    b = 'Not Chicago?'
    print(a + ' ' + b)
    print('{} {}'.format(a, b))
    print('hello' 'world')


def use_generator():
    print(','.join(str(s) for s in data))
    a = 'he'
    b = 'lala'
    c = 'mam'
    print(a + ':' + b + ':' + c)  # Ugly
    print(':'.join([a, b, c]))  # Still ugly
    print(a, b, c, sep=':')  # Better


# use_join()
use_generator()
