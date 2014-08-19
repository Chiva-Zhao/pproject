'''
Created on 19 Aug 2014

@author: cz186008
'''
import cgi
import athletemodel
import yate
import glob
import cgitb

cgitb.enable()
data_files = glob.glob("data/*.txt")
athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value
athlete = athletes[athlete_name]
print(yate.start_response())
print(yate.include_header("Athlete " + athlete_name + "Dob: " + athlete.dob + "."))
print("The top time for this athlete are:")
print(yate.u_list(athlete.top3))
links = {'Home': '/index.html', 'Select another athlete':'generate_list.py'}
print(yate.include_footer(links))
