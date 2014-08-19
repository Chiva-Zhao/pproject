'''
Created on 19 Aug 2014

@author: cz186008
'''
import athletemodel
import json
import yate

print(yate.start_response('application/json'))
names = athletemodel.get_names_from_store()
print(json.dumps(sorted(names)))
