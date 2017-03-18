# 你想排序类型相同的对象，但是他们不支持原生的比较操作

class User:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "user({})".format(self.id)


users = [User(11), User(22), User(9)]


def sort():
    print(users)
    print(sorted(users, key=lambda u: u.id))


def sort1():
    from operator import attrgetter
    print(sorted(users, key=attrgetter('id')))


sort()
sort1()
