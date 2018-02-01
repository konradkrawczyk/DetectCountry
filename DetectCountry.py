from GeoMaps import country_map

#Detect country from the list.
def detect_country(txt):


	votes = {}

	txt = txt.lower()
	#indicators = {}
	for country_indicator in country_map:
		found_countries =[]
		#You do not want a subset like India is in Indiana and CH is in Manchester. or Jersey is in New Jersey.
		temp_indicator = ' '+country_indicator.lower()+' '
			
		if temp_indicator.lower() in txt:
			found_countries = country_map[country_indicator]
			#indicators[temp_indicator] = country_indicator

		for country in found_countries:
			country = country.lower()+';'+temp_indicator
			#print country
			try:
				votes[country]+=1
			except KeyError:
				votes[country] = 1

	return votes

if __name__ == '__main__':
	#detect country

	txt = "University of Greek values"

	countries = detect_country(txt)

	print countries
