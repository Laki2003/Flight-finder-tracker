from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'entrance.html')

def pilot(request):
    return render(request, 'pilot.html')

def control(request):
    return render(request, 'control.html')