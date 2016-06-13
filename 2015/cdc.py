import requests
import json

tokens = json.load(open('tokens.json','r'))['socrata']
r = requests.get(
    "https://data.cdc.gov/resource/qpap-3u8w.json?$select=*", 
    headers={"X-App-Token":tokens['app']}
)
print r.json()

