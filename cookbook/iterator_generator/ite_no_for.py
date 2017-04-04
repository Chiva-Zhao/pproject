# 你想遍历一个可迭代对象中的所有元素，但是却不想使用 for 循环
# 为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异
# 常。比如，下面的例子手动读取一个文件中的所有行
def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                # line = next(f)
                line = next(f, None)
                if line is None:
                    break
                print(line, end='')
        except StopIteration:
            pass


items = [1, 2, 3]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
