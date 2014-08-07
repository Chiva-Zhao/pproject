'''
Created on 7 Aug 2014

@author: cz186008
'''
import pickle
from athletelist import AthleteList 
def get_coach_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readline().strip().split(',')
            return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as err:
        print("File error: " + str(err))
        return None

def put_to_store(file_list):
    athleteDic = {}
    for file in file_list:
        athlete = get_coach_data(file)
        athleteDic[athlete.name] = athlete
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(athleteDic, athf)
    except IOError as err:
        print('File error (put and store): ' + str(err))
    return athleteDic

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print('File error (get from store): ' + str(err))
    return all_athletes

the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
for each_athlete in data:
    print(data[each_athlete].name + ' ' + data[each_athlete].dob)