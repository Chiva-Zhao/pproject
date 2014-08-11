'''
Created on 11 Aug 2014

@author: cz186008
'''
def reverse(text):
    result = []
    while len(text) != 0:
        result.append(text[-1:])
        text = text[:len(text)-1]
    return ''.join(result)
print(reverse('Python'))