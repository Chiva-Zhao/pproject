# 解除一个装饰器
# 一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数。
# 假设装饰器是通过 @wraps来实现的，那么你可以通过访问__wrapped__属性来访问原始函数：
# 直接访问未包装的原始函数在调试、内省和其他函数操作时是很有用的。但是我们
# 这里的方案仅仅适用于在包装器中正确使用了 @wraps 或者直接设置了 wrapped 属
# 性的情况。
# 如果有多个包装器，那么访问 wrapped 属性的行为是不可预知的，应该避免这
# 样做。在 Python3.3 中，它会略过所有的包装层，比如，假如你有如下的代码：
from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


print(add(2, 3))
print(add.__wrapped__(2, 3))
# Decorator 2
# 5
# 最后要说的是，并不是所有的装饰器都使用了 @wraps ，因此这里的方案并不全部
# 适用。特别的，内置的装饰器 @staticmethod 和 @classmethod 就没有遵循这个约定
# (它们把原始函数存储在属性 func 中)。