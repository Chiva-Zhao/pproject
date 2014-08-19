'''
Created on 19 Aug 2014

@author: cz186008
'''
import cgi
import athletemodel
import yate
import json

athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
name = form_data['which_athlete'].value
print(yate.start_response('application/json'))
print(json.dumps(athletes[name].to_dict))