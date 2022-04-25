from audioop import tomono
import random
from time import strftime, strptime
from tokenize import Number
from xmlrpc.client import DateTime
from django.forms import DateField
from django.http import HttpResponse
from django.shortcuts import redirect, render

from search.graph import Grana, TezinskiGraf
from .models import Flight
from datetime import date
from datetime import timedelta
# Create your views here.
def index(request):
       return render(request, 'search.html')


def create_flight(request):
    return render(request, 'add_flight.html')

def create_flight_post(request):
    print(request.POST)
    [od, do] = [request.POST.get('od'), request.POST.get('do')]
    [monday, tuesday, wednesday, thursday, friday, saturday, sunday] = [
         bool(request.POST.get('monday')), bool(request.POST.get('tuesday')),
         bool(request.POST.get('wednesday')), bool(request.POST.get('thursday')),
         bool(request.POST.get('friday')), bool(request.POST.get('saturday')), 
         bool(request.POST.get('sunday')) 
    ]
    [vremeOd, vremeDo] = [request.POST.get('vremeOd'), request.POST.get('vremeDo')]
    [price, seats] = [float(request.POST.get('price')), int(request.POST.get('seats'))]
    baggage = bool(request.POST.get('baggage'))
    start_date = date(2022, 6, 1)
    while start_date < date(2022,9,1):
        if(date.weekday(start_date) == 0 and monday != 1):
            start_date += timedelta(days = 1)
            continue
        elif(date.weekday(start_date) == 1 and tuesday!=1):
            start_date += timedelta(days = 1)
            continue
        elif(date.weekday(start_date) == 2 and wednesday!=1):
            start_date += timedelta(days = 1)
            continue
        elif(date.weekday(start_date) == 3 and thursday!=1):
            start_date += timedelta(days = 1)
            continue
        elif(date.weekday(start_date) == 4 and friday!=1):
            start_date += timedelta(days = 1)
            continue
        elif(date.weekday(start_date) == 5 and saturday!=1):
            start_date += timedelta(days = 1)
            continue
        elif(date.weekday(start_date) == 6 and sunday!=1):
            start_date += timedelta(days = 1)
            continue
      
        priceE = random.uniform(price*0.77, price*1.77)
        priceB = priceE*1.45
        sedista = random.randint(int(seats*0.2), int(seats*1.2))
        start_date += timedelta(days = 1)
        flight = Flight(sifraLeta = od[0]+od[1]+do[0]+do[1]+str(random.randint(0, 1000000))+do+str(start_date), day = start_date, od = od, do = do, 
        cenaE = priceE, cenaB = priceB, brojMesta = sedista, prtljagE = baggage, 
        vremePolaska = vremeOd, vremeDolaska = vremeDo)
        flight.save()
        


    return redirect('/search/addFlight/')

def search(request):
    [od, do] = [request.GET.get('od'), request.GET.get('do')]
    [start_date, return_date] = [request.GET.get('startDate'), request.GET.get('returnDate')]
    flights = Flight.objects.filter(day = start_date)
    g = TezinskiGraf()
    htmlText = ""
    for f in flights:
        let = Grana(f.od, f.do, f.cenaE+f.brojMesta/100, f)
        g.dodaj_granu(let)

    g.ispisi_susedstva()
    if(od != '' and do!=''):
       htmlText = g.dijkstraForVertex(od, do)
    elif(od!='' and do==''):
      htmlText = g.dijkstra(od)
    elif(od=='' and do==''):
     htmlText = g.floyd_warshall()
  
    if(htmlText==""):
            htmlText = "<div class='card text-danger'>Nema leta/letova za unete datume/lokaciju.</div>"
    return render(request, 'results.html', {'htmlText' : htmlText})