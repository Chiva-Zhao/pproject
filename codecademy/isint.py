'''
Created on 10 Aug 2014

@author: cz186008
'''
def is_int(x):
    if type(x) == int:
        return True
    elif type(x) == float:
        str_num = str(x)
        posix_num = int(str_num[str_num.index('.')+1:])
        if posix_num == 0:
            return True
        else:
            return False
    else:
        return False

print(is_int(7.0))   # True
print(is_int(7.005))   # False
print(is_int(-1))    # True          