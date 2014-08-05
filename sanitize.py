'''
Created on 4 Aug 2014

@author: cz186008
'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string 
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)
    
