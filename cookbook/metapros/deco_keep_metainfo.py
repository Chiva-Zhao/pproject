# 创建装饰器时保留函数元信息
# 你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文
# 档字符串、注解和参数签名都丢失了。
# 任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注
# 解底层包装函数。例如：
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


# 下面我们使用这个被包装后的函数并检查它的元信息：
@timethis
def countdown(n: int):
    while n > 0:
        n -= 1


countdown(100000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
# 在编写装饰器的时候复制元信息是一个非常重要的部分。如果你忘记了使用 @wrap
# ，那么你会发现被装饰函数丢失了所有有用的信息。比如如果忽略 @wrap 后的效果是
# 下面这样的：
# >>> countdown.__name__
# 'wrapper'
# >>> countdown.__doc__
# >>> countdown.__annotations__
# {}
# @wraps 有一个重要特征是它能让你通过属性 wrapped 直接访问被包装函数。例如:
countdown.__wrapped__(100000)
# __wrapped__属性还能让被装饰函数正确暴露底层的参数签名信息。例如：
from inspect import signature
print(signature(countdown))
# 一个很普遍的问题是怎样让装饰器去直接复制原始函数的参数签名信息，如果想自
# 己手动实现的话需要做大量的工作，最好就简单的使用 wrapped 装饰器。通过底层
# 的 wrapped 属性访问到函数签名信息