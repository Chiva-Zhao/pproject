# 在类中定义多个构造器
# 你想实现一个类，除了使用 init () 方法外，还有其他方式可以初始化它。
import time


class Date:
    """ 方法一：使用类方法"""

    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


# 直接调用类方法即可，下面是使用示例：
a = Date(2012, 12, 21)  # Primary
print(a)
b = Date.today()  # Alternate
print(b)


# 类方法的一个主要用途就是定义多个构造器。它接受一个 class 作为第一个参数
# (cls)。你应该注意到了这个类被用来创建并返回最终的实例。在继承时也能工作的很好：
class NewDate(Date):
    pass


c = Date.today()  # Creates an instance of Date (cls=Date)
d = NewDate.today()  # Creates an instance of NewDate (cls=NewDate)