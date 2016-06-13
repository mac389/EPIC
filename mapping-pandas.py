import json, vincent 
import pandas as pd

with open('us_states.topo.json', 'r') as f:
    get_id = json.load(f)

df = pd.read_csv('prevalence.csv',na_values=[' '])
geo_data = [{'name':'states','url':'us_states.topo.json','feature':'us_states.geo'}]

vis = vincent.Map(data=df,geo_data=geo_data,scale=1000,projection='albersUsa', data_bind='Prevalence', 
		data_key='Prevalence', map_key={'states':'properties.NAME'})

vis.display()

vis.to_json('vega.json', html_out=True,html_path='vega_tmp.html')
