# deque
from collections import deque

d = deque()
d.append(1)
d.append('2')
d.append('3')
print(d)
print(len(d))
print(d[0])
print(d[-1])

d = deque(range(5))
print(d)
print(d.popleft())
print(d.pop())
print(d)

d = deque(maxlen=5)
for i in range(10):
    d.append(i)
print(d)

d = deque([1, 2, 3, 4, 5])
d.extendleft([1, 2, 3])
d.extend([9, 8, 7])
print(d)
