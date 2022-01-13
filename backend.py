import json
from amadeus import Client, ResponseError


def pretrazi():
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

pretrazi()






