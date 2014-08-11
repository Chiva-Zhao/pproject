'''
Created on 7 Aug 2014

@author: cz186008
'''

import athletemodel
import yate
import glob

data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)
print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.para("Select an athlete from the list to work with:"))
print(yate.start_form("generate_timing_data.py"))
for athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[athlete].name))
print(yate.end_form("Select"))
print(yate.include_footer({'home':'/index.html'}))