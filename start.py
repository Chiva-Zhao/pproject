'''
Created on 4 Aug 2014

@author: cz186008
'''
james = [];julie = [];mikey = [];sarah = [];

try:
    with open("james.txt", "r") as jamesdata, open("julie.txt", "r") as juliedata, open("mikey.txt", "r") as mikeydata, open("sarah.txt", "r") as sarahdata:
        for line in jamesdata:
            james = line.strip().split(',')
        for line in juliedata:
            julie = line.strip().split(',')
        for line in mikeydata:
            mikey = line.strip().split(',')
        for line in sarahdata:
            sarah = line.strip().split(',')
except IOError as err:
    print(str(err))
print(james)
print(julie)
print(mikey)
print(sarah)

