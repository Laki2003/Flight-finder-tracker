from django.forms import DateField
from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    let = Flight(sifraLeta = "adfassdgsd", day = "2022-02-22", od = "London", do="Pariz", cenaE = 120.2, brojMesta = 200, cenaB=5212, prtljagE = True, vremePolaska = "13:30", vremeDolaska = "17:30")
    let.save()
    return render(request, 'search.html')

def createFlight(request):
    print(request.POST)
    [od, do] = [request.POST.get('od'), request.POST.get('do')]
    [monday, tuesday, wednesday, thursday, friday, saturday, sunday] = [
        bool(request.POST.get('monday')), bool(request.POST.get('tuesday')),
         bool(request.POST.get('wednesday')), bool(request.POST.get('thursday')),
         bool(request.POST.get('friday')), bool(request.POST.get('saturday')), 
         bool(request.POST.get('sunday')) 
    ]
    [vremeOd, vremeDo] = [request.POST.get('vremeOd'), request.POST.get('vremeDo')]

    print(monday, tuesday, wednesday, thursday, friday, saturday, sunday)
    print(vremeOd, vremeDo)
    return render(request, 'add_flight.html')