'''
Created on 11 Aug 2014

@author: cz186008
'''
def censor(text,word):
    rep_word = '*' * len(word)
    return text.replace(word,rep_word)