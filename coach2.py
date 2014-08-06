'''
Created on 5 Aug 2014

@author: cz186008
'''
def sanitize(timeString):
    if '-' in timeString:
        splitter = '-'
    elif ':' in timeString:
        splitter=':'
    else:
        return timeString
    (minute,second) = timeString.split(splitter)
    return minute + '.' + second

def get_coach_data(filename):
    try:
        with open(filename,'r') as file:
            data = file.readline().strip().split(',')
            mapData = {}
            mapData['name'] = data.pop(0)
            mapData['date'] = data.pop(0)
            mapData['times'] = str(sorted(set([sanitize(time) for time in data]))[0:3])
            return mapData
    except IOError as err:
        print("File error: " + str(err))
        return None
    
# james = get_coach_data('sarah2.txt')
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

# (name,dob) = james.pop(0),james.pop(0)
# print(name + "'s fast times on " + dob + " are: " + str(sorted(set([sanitize(time) for time in james]))[0:3]))    
# print(map['name'] + "'s fast times on " + map['date'] + " are: " + str(sorted(set([sanitize(time) for time in map['times']]))[0:3]))    
print(james['name'] + "'s fast times on " + james['date'] + " are: " + james['times'])
print(julie['name'] + "'s fast times on " + julie['date'] + " are: " + julie['times'])
print(mikey['name'] + "'s fast times on " + mikey['date'] + " are: " + mikey['times'])
print(sarah['name'] + "'s fast times on " + sarah['date'] + " are: " + sarah['times'])