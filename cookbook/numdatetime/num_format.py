# 需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符
x = 1234.56789


def simple_format():
    # Two decimal places of accuracy
    print(format(x, '0.2f'))
    # Right justified in 10 chars, one-digit accuracy
    print(format(x, '>10.1f'))
    # Left justified
    print(format(x, '<10.1f'))
    # Centered
    print(format(x, '^10.1f'))
    print(format(x, 'e'))
    print(format(x, '0.2E'))
    print('The value is {:0,.2f}'.format(x))


simple_format()
