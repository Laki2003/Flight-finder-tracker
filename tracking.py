import requests
import json
from graph import Graph
#params = {
 #   'api_key': '2cb005fd-df55-4f4d-b798-b07534695216',
#    "icao_code": "EDI",
#    "country_code": "UK"
#    
#}
#method = 'ping'
#api_base = 'https://airlabs.co/api/v9/flights?'
#api_result = requests.get(api_base+method, params)
#api_response = api_result.json()


params = {
    'api_key': '2cb005fd-df55-4f4d-b798-b07534695216',
    "city_code": "BUD"
    
}
method = 'ping'
api_base = 'https://airlabs.co/api/v9/cities?'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()


print(json.dumps(api_response, indent=4, sort_keys=True))

def proba():
    g = Graph()
    g.add_vertex("LON")
    g.add_vertex("BUD")
    g.add_edge("LON", "BUD", 7)
    g.printGraph()

proba()



