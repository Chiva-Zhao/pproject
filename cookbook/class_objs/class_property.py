# 创建可管理的属性
# 你想给某个实例 attribute 增加除访问与修改之外的其他处理逻辑，比如类型检查/或合法性验
# 自定义某个属性的一种简单方法是将它定义为一个 property。例如，下面的代码定
# 义了一个 property，增加对一个属性简单的类型检查：
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


# 上述代码中有三个相关联的方法，这三个方法的名字都必须一样。第一个方法是一
# 个 getter 函数，它使得 first name 成为一个属性。其他两个方法给 first name 属
# 性添加了 setter 和 deleter 函数。需要强调的是只有在 first name 属性被创建后，
# 后面的两个装饰器 @first name.setter 和 @first name.deleter 才能被定义。
# property 的一个关键特征是它看上去跟普通的 attribute 没什么两样，但是访问它
# 的时候会自动触发 getter 、 setter 和 deleter 方法。例如：
a = Person('Guido')
print(a.first_name)  # Calls the getter
# a.first_name = 42  # Calls the setter
# del a.first_name

# 一个 property 属性其实就是一系列相关绑定方法的集合。如果你去查看拥有
# property 的类，就会发现 property 本身的 fget、 fset 和 fdel 属性就是类里面的普通方
# 法。比如：
print(Person.first_name.fget)
print(Person.first_name.fset)
print(Person.first_name.fdel)


# 通常来讲，你不会直接取调用 fget 或者 fset，它们会在访问 property 的时候自动
# 被触发。
# 只有当你确实需要对 attribute 执行其他额外的操作的时候才应该使用到 property。
# 有时候一些从其他编程语言 (比如 Java) 过来的程序员总认为所有访问都应该通过
# getter 和 setter，所以他们认为代码应该像下面这样写：
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
# 不要写这种没有做任何其他额外操作的 property。首先，它会让你的代码变得很
# 臃肿，并且还会迷惑阅读者。其次，它还会让你的程序运行起来变慢很多。最后，这
# 样的设计并没有带来任何的好处。特别是当你以后想给普通 attribute 访问添加额外
# 的处理逻辑的时候，你可以将它变成一个 property 而无需改变原来的代码。因为访问
# attribute 的代码还是保持原样。
# Properties 还是一种定义动态计算 attribute 的方法。这种类型的 attributes 并不会
# 被实际的存储，而是在需要的时候计算出来。比如：



# 在实现一个 property 的时候，底层数据 (如果有的话) 仍然需要存储在某个地方。
# 因此，在 get 和 set 方法中，你会看到对 first name 属性的操作，这也是实际数据保
# 存的地方。另外，你可能还会问为什么 init () 方法中设置了 self.first name 而
# 不是 self. first name 。在这个例子中，我们创建一个 property 的目的就是在设置
# attribute 的时候进行检查。因此，你可能想在初始化的时候也进行这种类型检查。通
# 过设置 self.first name ，自动调用 setter 方法，这个方法里面会进行参数的检查，
# 否则就是直接访问 self. first name 了。
# 还能在已存在的 get 和 set 方法基础上定义 property。例如：
class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)
