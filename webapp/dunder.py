print("we start off on" + __name__)
if (__name__ == '__main__'):
    print('And end up on:' + __name__)


def outer():
    def inner():
        print('inner')

    print('outer')
    return inner


def myfunc(*args):
    for a in args:
        print(a, end=' ')


values = ['a', 'b', 1, 2, 3, 4, 6]
myfunc(*values)
