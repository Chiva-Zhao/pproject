some_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
for counter, value in enumerate(some_list):
    print(counter, value)
my_list = ['apple', 'banana', 'grapes', 'pear']
# 索引从1开始
for c, value in enumerate(my_list, 1):
    print(c, value)
print(list(enumerate(my_list, 1)))
