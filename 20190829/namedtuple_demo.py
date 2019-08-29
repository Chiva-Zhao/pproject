man = ('Ali', 30)
print(man[0])
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry)
print(perry.name)
# perry.age=20 #AttributeError: can't set attribute
print(perry[1])
# 转换为字典
print(perry._asdict())
