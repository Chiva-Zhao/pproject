'''
Created on 11 Aug 2014

@author: cz186008
'''
def anti_vowel(text):
    vowels = 'aeiou'
    result = []
    for ch in text:
        if vowels.find(ch.lower()) == -1:
            result.append(ch)
    return ''.join(result)