import folium, os, random, csv, json   
import pandas as pd

NYC_COORDINATES = (40.7128,-74.0059)
DATA_PATH = '../../data'
NYC_map_file = os.path.join(DATA_PATH,'map.geo.json')
map_data = json.load(open(NYC_map_file,'rb'))

boros = [item['properties']['BoroName'] 
   for item in map_data['features']]
activity = {boro:random.randint(0,100) for boro in boros}
'''
activity = [(boro,random.randint(0,100)) for boro in boros]
   d = {"a":"b","c":"d"}
   d.keys() => ["a"]
   d.values() => ["b"]
   d.items() => [("a","b"),("c","d")]
'''

df = pd.DataFrame(activity.items(),columns = ["Boro","Activity"])
df.to_csv(os.path.join(DATA_PATH,'activity.csv'), index=False)

#Let Folium determine the scale
print map_data['features'][0]['properties']['BoroName']
#{"Brooklyn":stuff,"SI":stuff}
#[{name:"Brooklyn",contents:stuff},{name:"SI",contents:garbage}]
folium_map = folium.Map(location=NYC_COORDINATES, zoom_start=12)
folium_map.choropleth(geo_path = NYC_map_file,
				data = df,
	             columns=['Boro','Activity'],
    	         key_on='feature.properties.BoroName',
        	     fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,)

folium_map.save('test.html')