'''
Created on 11 Aug 2014

@author: cz186008
'''
def is_prime(x):
    if x== 0 or x == 1:
        return False
    x = abs(x)
    for n in range(2,x-1):
        if x%n == 0:
            return False
    return True

print(is_prime(-7))