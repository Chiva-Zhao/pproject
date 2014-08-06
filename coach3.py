'''
Created on 6 Aug 2014

@author: cz186008
'''
class Athlete:
    def __init__(self,a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]
    
    def add_time(self,time):
        self.times.append(time)
    
    def add_times(self,timelists):
        self.times.extend(timelists)
            
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (minute,second) = time_string.split(splitter)
    return minute + '.' + second
        
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return Athlete(templ.pop(0),templ.pop(0),templ)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)
    
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

''' Testing for add_time and add_times'''
vera = Athlete('Vera Vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1-21','2:22'])
print(vera.top3())