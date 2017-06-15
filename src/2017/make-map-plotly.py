import os, json 

import plotly.plotly as py 
import plotly.graph_objs as graph_objs

DATA_PATH = '../../data'
NYC_map_file = os.path.join(DATA_PATH,'map.geo.json')
activity = os.path.join(DATA_PATH,'NYC-activity.json')

NYC_map = json.load(open(NYC_map_file,'rb'))
mapbox_access_token = json.load(open(os.path.join(DATA_PATH,'directory.json'),'rb'))['mapbox']


data = graph_objs.Data([
    graph_objs.Scattermapbox(
        lat=['40.5017'],
        lon=['74.5673'],
        mode='markers',
    )
])
layout = graph_objs.Layout(
    height=600,
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        layers=[
            dict(
                sourcetype = 'geojson',
                source = NYC_map_file,
                type = 'fill',
                color = 'rgba(163,22,19,0.8)'
            ),
            dict(
                sourcetype = 'geojson',
                source = activity,
                type = 'fill',
                color = 'rgba(40,0,113,0.8)'
            )
        ],
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.7128,
            lon=-74.0059
        ),
        pitch=0,
        zoom=11.25,
        style='light'
    ),
)

fig = dict(data=data, layout=layout)
print py.plot(fig, filename='county-level-choropleths-python')
