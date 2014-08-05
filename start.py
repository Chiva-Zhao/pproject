'''
Created on 4 Aug 2014

@author: cz186008
'''
# james = [];julie = [];mikey = [];sarah = [];
import sanitize
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
# data = [];    
# for time in james:
#     data.append(sanitize.sanitize(time))
james = sorted(set([sanitize.sanitize(time) for time in james]))

# data.clear()
# for time in julie:
#     data.append(sanitize.sanitize(time))
julie = sorted(set([sanitize.sanitize(time) for time in julie]))

# data.clear()
# for time in mikey:
#     data.append(sanitize.sanitize(time))
mikey = sorted(set([sanitize.sanitize(time) for time in mikey]))

# data.clear()
# for time in sarah:
#     data.append(sanitize.sanitize(time))
sarah = sorted(set([sanitize.sanitize(time) for time in sarah]))
print(james)
print(julie)
print(mikey)
print(sarah)

