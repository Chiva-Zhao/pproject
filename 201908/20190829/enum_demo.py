from collections import namedtuple
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    kitten = 1  # (幼⼩的猫咪)
    puppy = 2  # (幼⼩的狗狗)


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

print(charlie.type == perry.type)
print(charlie.type)
print(Species(1))
print(Species(9))
print(Species.cat)
print(Species['cat'])
print(Species.kitten)
print(Species.puppy)