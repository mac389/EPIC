from pygeocoder import Geocoder
import us, csv, json

WRITE = 'wb'
READ = 'rb'

#corpus = json.load(open('bieber-raw-test.json',READ))
corpus = json.load(open('sxsw-SXSW-#SXSW-#sxsw-20140308-001535.json',READ))
def get_location(tweet):
	if tweet['coordinates']:
		lat,lon = tuple(tweet['coordinates']['coordinates'])
		try:
			location = Geocoder.reverse_geocode(lat,lon)
			if location.state == 'United States':
				return us.states.lookup(location.administrative_area_level_1).abbr.strip()
		except:
			pass
	elif tweet['place']:
		return tweet['place']['full_name'].split(',')[-1].strip()


locations = [get_location(tweet) for tweet in corpus] 
print filter(None,locations)
states = [state.abbr for state in us.states.STATES]
prevalence = {state:count for state,count in zip(states,[locations.count(state) for state in states])}
print prevalence

with open('prevalence.csv', 'wb') as f:
	for state,count in prevalence.items():
		print>>f,'%s,%d'%(state,count)
