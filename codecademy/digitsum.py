'''
Created on 11 Aug 2014

@author: cz186008
'''
def digitsum(n):
    result = 0
    str_n = str(n)
    for s in str_n:
        result += int(s)
    return result
print(digitsum(434))