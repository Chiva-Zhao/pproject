# 可接受任意数量参数的函数
# 为了能让一个函数接受任意数量的位置参数，可以使用一个 * 参数。
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# Sample use
print(avg(1, 2))  # 1.5
print(avg(1, 2, 3, 4))  # 2.5
# 为了接受任意数量的关键字参数，使用一个以 ** 开头的参数
import html


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name,
                                                       attrs=attr_str,
                                                       value=html.escape(value))
    return element


# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))
# Creates '<p>&lt;spam&gt;</p>'
print(make_element('p', '<spam>'))


# 在这里， attrs 是一个包含所有被传入进来的关键字参数的字典。
# 如果你还希望某个函数能同时接受任意数量的位置参数和关键字参数，可以同时使用 * 和 **
def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict


# 一个 * 参数只能出现在函数定义中最后一个位置参数后面，而**参数只能出现在
# 最后一个参数。有一点要注意的是，在 * 参数后面仍然可以定义其他参数
def a(x, *args, y):
    pass


def b(x, *args, y, **kwargs):
    pass
# 这种参数就是我们所说的强制关键字参数