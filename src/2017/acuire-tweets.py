import json, datetime


from TwitterAPI import TwitterAPI

directory = json.load(open('../../data/directory.json','rb'))
keys = directory['credentials']

api = TwitterAPI(keys['consumer_key'], keys['consumer_secret'], 
				keys['access_token'], keys['access_token_secret'])

query = 'aids'
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
outfile = '../../data/%s-%s'%(query,timestamp)
r = api.request('search/tweets', {'q':'aids'})

with open(outfile,'wb') as outfile:
	for item in r:
		print>>outfile,item
		#json.dump(item,outfile)

'''
r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
for item in r:
		print(item)
'''