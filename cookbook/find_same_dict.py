a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# same_key = set(a.keys()).intersection(set(b.keys()))
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
same_value = set(a.values()).intersection(set(b.values()))
# print(a.values() & b.values())
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
