'''
Created on 11 Aug 2014

@author: cz186008
'''
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum
def grades_average(grades):
    sum = grades_sum(grades)
    length = float(len(grades))
    return sum/length
print(grades_average(grades))    