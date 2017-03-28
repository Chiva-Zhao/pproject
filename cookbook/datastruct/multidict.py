from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
d['b'].append(3)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

pairs = {'a': 1, 'a': 2, 'b': 3, 'b': 4}
print(pairs)
