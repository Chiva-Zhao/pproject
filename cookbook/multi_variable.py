p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)
name, shares, price, (year, mon, day) = data
print(name, shares, price, year, mon, day)
_, shares, price, _ = data
print(shares, price)

s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phones = record
print(name, email, phones)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(current, trailing)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *field, home, sh = line.split(":")
print(uname, home, sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)
items = [1, 10, 7, 4, 5, 9]


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))
