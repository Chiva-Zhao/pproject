# 在关系型数据库中查询、增加或删除记录
import sqlite3

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

db = sqlite3.connect("mydb")
c = db.cursor()
c.execute('DROP TABLE portfolio')
c.execute('CREATE TABLE portfolio (symbol TEXT, shares INTEGER, price REAL)')
db.commit()
c.executemany('INSERT INTO portfolio VALUES (?,?,?)', stocks)
db.commit()
for row in c.execute("SELECT * FROM portfolio"):
    print(row)
# 如果你想接受用户输入作为参数来执行查询操作，必须确保你使用下面这样的占位
# 符 ‘‘?‘‘来进行引用参数
min_price = 100
for row in db.execute('SELECT * FROM portfolio WHERE price >= ?', (min_price,)):
    print(row)
