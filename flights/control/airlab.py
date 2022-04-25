import requests
import json





def findFlight(iata):

    params = {
        'api_key': '0146375f-70c0-4723-a882-767093b36f4f',
       'flight_iata': iata
    }

    method = 'get'
    api_base = 'https://airlabs.co/api/v9/flight?'
    api_result = requests.get(api_base+method, params)
    try:
     api_response = api_result.json()['response']
    except KeyError:
        return None

    print(api_response)

    return api_response


def findNearAirports(flight):
   
    
    params = {
        'api_key': '0146375f-70c0-4723-a882-767093b36f4f',
        'lat': flight['lat'],
        'lng': flight['lng'],
        'distance': 200


    }
    method = 'get'
    api_base = 'https://airlabs.co/api/v9/nearby?'
    api_result = requests.get(api_base+method, params)
    api_response = api_result.json()['response']['airports']
    print(api_response)
    return api_response

def getAirportInfo(iataCode):

    params = {
        'api_key': '0146375f-70c0-4723-a882-767093b36f4f',
        'iata_code': iataCode,
        '_fields': "name, lat, lng"
    }
    method = 'get'
    api_base = 'https://airlabs.co/api/v9/airports?'
    airport = requests.get(api_base+method, params).json()['response'][0]
    print(airport)
    return airport

