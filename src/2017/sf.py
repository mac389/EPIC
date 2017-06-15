import folium
import pandas as pd

NYC_COORDINATES = (40.7128,-74.0059)
#crimedata = pd.read_csv('SFPD_Incidents_-_Current_Year__2015_.csv')

 
# create empty map zoomed in on San Francisco
folium_map = folium.Map(location=NYC_COORDINATES, zoom_start=12)

'''
# add a marker for every record in the filtered data, use a clustered view
for each in crimedata[0:MAX_RECORDS].iterrows():
    map.simple_marker(
        location = [each[1]['Y'],each[1]['X']], 
        clustered_marker = True)
 '''
folium_map.save('test.html') 