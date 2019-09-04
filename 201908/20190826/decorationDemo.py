from functools import wraps


def deco_fun(exeFun):
    # @wraps接受
    # ⼀个函数来进⾏装饰， 并加⼊了复制函数名称、 注释⽂档、 参数列表
    # 等等的功能。 这可以让我们在装饰器⾥⾯访问在装饰之前的函数的属性
    @wraps(exeFun)
    def wrapper():
        print("befre execute")
        exeFun()
        print("after execute")
    return wrapper

def needDeco():
    print("my fun execute")

fun1 = deco_fun(needDeco)
fun1();

@deco_fun
def needDeco1():
    """装饰器调用"""
    print("my fun execute1")
needDeco1()
print(needDeco1.__name__);