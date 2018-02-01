import csv
from os.path import join



#Fetch adjectives describing countries.
def fetch_adjectives():


	adjectives= {}
	with open(join('data','adjectives.csv')) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			adjectives[row[0]] = row[1]

	return adjectives

#Fetch the detailed locations
def fetch_locations():

	countries = {}
	cities = {}
	regions = {}

	with open(join('data','locations.csv')) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			country = row[4].lower()
			region = row[6].lower()
			city = row[7].lower()
			countries[country] = country
			regions[region] = country
			regions[city] = country

	return countries,cities,regions

#The master mapping for the detector.
def fetch_mapping():
	adjectives = fetch_adjectives()
		
	countries,cities,regions = fetch_locations()


	mapping = {'country':{
				'score':10,
				'map': countries
			     },
		   'city':{
				'score':1,
				'map': cities
			     },
		   'region':{
				'score':1,
				'map': regions
			     },
		   'adjective':{
				'score':10,
				'map': adjectives
			     }
		}
	return mapping
	

#Detect country from the list.
def detect_country(txt):


	votes = {}

	txt = ' '+txt.lower().replace(',','').replace('.','')+' '
	#Our mappings.
	mappings = fetch_mapping()
	#indicators = {}
	for mapping in mappings:
		current_mapping = mappings[mapping]
		print 'Current mapping',mapping
		for country_indicator in current_mapping['map']:
			
			
			found_countries =[]
			#You do not want a subset like India is in Indiana and CH is in Manchester. or Jersey is in New Jersey.
			temp_indicator = ' '+country_indicator.lower()+' '
			
			if temp_indicator in txt:
				
				country = current_mapping['map'][country_indicator]
				country = country.lower()#+';'+temp_indicator
				
				try:
					votes[country]+=current_mapping['score']
				except KeyError:
					votes[country] = current_mapping['score']

	return votes

if __name__ == '__main__':
	
	print detect_country('University of Oxford, United Kingdom')
	
