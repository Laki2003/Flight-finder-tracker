from math import sqrt, sin, cos, atan2, radians
from contextvars import Context
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
from control.airlab import findFlight, findNearAirports, getAirportInfo
from control.graph import Grana, TezinskiGraf




# Create your views here.
def index(request):

    return render(request, 'entrance.html')

def pilot(request):
    iataCode = request.GET.get('iataCode')
    return render(request, 'pilot.html',{"iataCode": iataCode})
def distance(x1, y1, x2, y2):
    R = 6373.0
    dlon = x1-x2
    dlat = y1-y2
    a = sin(dlat/2)**2 + cos(y1)*cos(y2)*sin(dlon/2)**2
    c = 2*atan2(sqrt(a), sqrt(1-a))
    return R*c
    
def  control(request):
    iataCode = request.GET.get('iataCode')
    flight = findFlight(iataCode)
    if(flight==None):
        return render(request, 'control.html', {'htmlText':''' <div class="alert alert-danger" role="alert">
        <h1>Ukucali ste pogresnu sifru leta ili se taj avion ne nalazi u vazduhu</h1></div>'''})
    arrivalAirport = getAirportInfo(flight['arr_iata'])
    razdaljina = distance(flight['lng'], flight['lat'], arrivalAirport['lng'], arrivalAirport['lat'])
    g = TezinskiGraf()
 
    grana1 = Grana("avion", arrivalAirport["name"], razdaljina)
    g.dodaj_granu(grana1)
    aerodromi = findNearAirports(flight)
    for a in aerodromi:
        grana2=Grana("avion", a['name'], a['distance']+a['popularity']/1000)
        grana3= Grana(a['name'], arrivalAirport['name'], distance(a['lng'], a['lat'], arrivalAirport['lng'], arrivalAirport['lat']))
        g.dodaj_granu(grana2)
        g.dodaj_granu(grana3)
    
    htmlText = g.dijkstra("avion", arrivalAirport['name'])
    return render(request, 'control.html', {'htmlText':  '<div class="alert alert-success" role="alert">' + g.dijkstra("avion", arrivalAirport['name']) + '</div>'})
