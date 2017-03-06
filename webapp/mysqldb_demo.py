import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'zzh',
            'password': 'zzh',
            'database': 'pydb', }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
cursor.execute("show tables")
rst = cursor.fetchall()
print(rst)

cursor.execute("describe log")
rst = cursor.fetchall()
for item in rst:
    print(item)
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""
cursor.execute(_SQL)

_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
(%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))
conn.commit()

_SQL = '''select * from log'''
cursor.execute(_SQL)
rst = cursor.fetchall()
for r in rst:
    print(r)
cursor.close()
conn.close()
