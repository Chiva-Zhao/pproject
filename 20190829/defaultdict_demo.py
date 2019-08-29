from collections import defaultdict
# defaultdict
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
favourite_colours = defaultdict(list)
for name, color in colours:
    favourite_colours[name].append(color)
print(favourite_colours)

some_dict = {}
# some_dict['colours']['favourite'] = "yellow" #KeyError: 'colours'
import collections

tree = lambda : collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
import json

print(json.dumps(some_dict))