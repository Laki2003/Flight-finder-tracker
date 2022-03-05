import json
import requests
import json
from graph import Graph
from amadeus import Client, ResponseError


def findFlight():
    datumPolaska = input('Unesi datum polaska ')
    datumOdlaska = input('nUnesi datum odlaska ')
    pocetak = input("Unesi grad odakle kreces ")
    destinacija = input("Unesi destinaciju ")
    brojPutnika = input("Unesi broj putnika ")


    amadeus = Client(
        client_id='xlGMzr0jJUSkR22IvxPlYanXhxQugRjR',
        client_secret='ZzFCx1MmIUAkqhHc'
    )

    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode= pocetak,
            destinationLocationCode=destinacija,
            departureDate= datumPolaska,
            nonStop="true",
            max = 7,
            adults=brojPutnika)
        jsondata = response.result
        print(json.dumps(jsondata["data"], indent = 4))
    except ResponseError as error:
        print(error)

def liveFlights(number):
    


    params = {
    'api_key': '2cb005fd-df55-4f4d-b798-b07534695216',
    'flight_icao': number
    
    }
    method = 'ping'
    api_base = 'https://airlabs.co/api/v9/flight?'
    api_result = requests.get(api_base+method, params)
    api_response = api_result.json()


    print(json.dumps(api_response, indent=4, sort_keys=True))






def findAirport(longitude, latitude, distance):
    g = Graph()
    g.add_vertex("plane")  
    params = {
        'api_key': '2cb005fd-df55-4f4d-b798-b07534695216',
        'lat': latitude,
        'lng': longitude,
        'distance': distance

    }
    method = 'ping'
    api_base = 'https://airlabs.co/api/v9/nearby?'
    api_result = requests.get(api_base+method, params)
    api_response = api_result.json()['response']['airports']
    
    for i in api_response:
             g.add_edge("plane", i["name"], i["distance"]+i["popularity"]/10000)
    
    for v in g:
        for w in v.get_connections():
            vid = v.get_name()
            wid = w.get_name()
            print(vid, wid, v.get_weight(w))


findAirport( -84.325283,40.039549, 200)

