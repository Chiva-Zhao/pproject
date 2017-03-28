# 映射名称到序列元素
from collections import namedtuple


def default():
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('jonesy@example.com', '2012-10-19')
    print(sub)
    print(sub.addr, sub.joined, len(sub))
    addr, join = sub
    print(addr, join)


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


def namedTest():
    s = Stock('ACME', 100, 123.45)
    print(s)
    print(s.price)
    # s.price = 100 一个命名元组是不可更改的
    # 如果你真的需要改变然后的属性，那么可以使用命名元组实例的replace()方法，
    # 它会创建一个全新的命名元组并将对应的字段用新的值取代。比如：
    s = s._replace(shares=200)
    print(s)


def replace():
    Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
    # Create a prototype instance
    stock_prototype = Stock('', 0, 0.0, None, None)

    # Function to convert a dictionary to a Stock
    def dict_to_stock(s):
        return stock_prototype._replace(**s)

    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(a))
    print(dict_to_stock(b))

replace()
