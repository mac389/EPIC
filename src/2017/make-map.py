import ast, vincent,os

DATA_PATH = '../../data' 

'''
tweets = map(ast.literal_eval,
			open('../../data/aids-test2.json','rb').read().splitlines())

coordinates = [tweet['geo'] for tweet in tweets]
print coordinates
'''

NYC_map_file = '../../data/map.topo.json'

geo_data = [{'name':'boros',
				'url': NYC_map_file,
             'feature': 'collection'}]

NYC = vincent.Map(geo_data=geo_data, scale=200)
NYC.to_json(os.path.join(DATA_PATH,'NYC.json'),html_out=True, 
			html_path=os.path.join(DATA_PATH,'NYC_map_template.html'))