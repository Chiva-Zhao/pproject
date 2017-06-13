# 利用装饰器强制函数上的类型检查
# 作为某种编程规约，你想对函数参数进行强制类型检查。
# 在演示实际代码前，先说明我们的目标：能对函数参数类型进行断言，类似下面这样：
# @typeassert(int, int)
# def add(x, y):
#     return x + y
# add(2, 3)
# add(2, 'hello')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "contract.py", line 33, in wrapper
# TypeError: Argument y must be <class 'int'>
# 下面是使用装饰器技术来实现 @typeassert ：
from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def docorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func
        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)

        return wrapper

    return docorate


# 可以看出这个装饰器非常灵活，既可以指定所有参数类型，也可以只指定部分。并
# 且可以通过位置或关键字来指定参数类型。下面是使用示例：
@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


spam(1, 2, 3)
spam(1, 'hello', 3)


# spam(1, 'hello', 'world')  # TypeError: Argument z must be <class 'int'>


# 这节是高级装饰器示例，引入了很多重要的概念。
# 首先，装饰器只会在函数定义时被调用一次。有时候你去掉装饰器的功能，那么你
# 只需要简单的返回被装饰函数即可。下面的代码中，如果全局变量　 debug 被设置
# 成了 False(当你使用 -O 或 -OO 参数的优化模式执行程序时)，那么就直接返回未修改
# 过的函数本身：
# def decorate(func):
#     # If in optimized mode, disable type checking
#     if not __debug__:
#         return func
# 其 次， 这 里 还 对 被 包 装 函 数 的 参 数 签 名 进 行 了 检 查， 我 们 使 用 了
# inspect.signature() 函数。简单来讲，它运行你提取一个可调用对象的参数签名
# 信息。例如：
# >>> from inspect import signature
# >>> def spam(x, y, z=42):
# ... pass
# ...
# >>> sig = signature(spam)
# >>> print(sig)
# (x, y, z=42)
# >>> sig.parameters
# mappingproxy(OrderedDict([('x', <Parameter at 0x10077a050 'x'>),
# ('y', <Parameter at 0x10077a158 'y'>), ('z', <Parameter at 0x10077a1b0 'z'>)]))
# >>> sig.parameters['z'].name
# 'z'
# >>> sig.parameters['z'].default
# 42
# >>> sig.parameters['z'].kind
# <_ParameterKind: 'POSITIONAL_OR_KEYWORD'>

# 装饰器的开始部分，我们使用了 bind partial() 方法来执行从指定类型到名称的
# 部分绑定。下面是例子演示：
# >>> bound_types = sig.bind_partial(int,z=int)
# >>> bound_types
# <inspect.BoundArguments object at 0x10069bb50>
# >>> bound_types.arguments
# OrderedDict([('x', <class 'int'>), ('z', <class 'int'>)])
# 在这个部分绑定中，你可以注意到缺失的参数被忽略了 (比如并没有对 y 进行绑
# 定)。不过最重要的是创建了一个有序字典 bound types.arguments 。这个字典会将参
# 数名以函数签名中相同顺序映射到指定的类型值上面去。在我们的装饰器例子中，这
# 个映射包含了我们要强制指定的类型断言。
# 在 装 饰 器 创 建 的 实 际 包 装 函 数 中 使 用 到 了 sig.bind() 方 法。 bind() 跟
# bind partial() 类似，但是它不允许忽略任何参数。因此有了下面的结果：
# >>> bound_values = sig.bind(1, 2, 3)
# >>> bound_values.arguments
# OrderedDict([('x', 1), ('y', 2), ('z', 3)])
# 使用这个映射我们可以很轻松的实现我们的强制类型检查：
# 不过这个方案还有点小瑕疵，它对于有默认值的参数并不适用。比如下面的代码可
# 以正常工作，尽管 items 的类型是错误的：

@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


bar(2)
# bar(2, 3)
print(bar(4, [1, 2, 3]))
# 最后一点是关于适用装饰器参数和函数注解之间的争论。例如，为什么不像下面这
# 样写一个装饰器来查找函数中的注解呢？
# 一个可能的原因是如果使用了函数参数注解，那么就被限制了。如果注解被用来做
# 类型检查就不能做其他事情了。而且 @typeassert 不能再用于使用注解做其他事情的
# 函数了。而使用上面的装饰器参数灵活性大多了，也更加通用。
