# 带有外部状态的生成器函数
# 你想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值
# 如果你想让你的生成器暴露外部状态给用户，别忘了你可以简单的将它实现为一个
# 类，然后把生成器函数放到 iter () 方法中
from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


# 为了使用这个类，你可以将它当做是一个普通的生成器函数。然而，由于可以创建
# 一个实例对象，于是你可以访问内部属性值，比如 history 属性或者是 clear() 方法
with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
