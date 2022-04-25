from venv import create
from django.db import models

class Flight(models.Model):
    sifraLeta = models.CharField(max_length = 30, primary_key=True)
    day = models.DateField()
    od = models.CharField(max_length=30)
    do = models.CharField(max_length=30)
    cenaE = models.FloatField()
    brojMesta = models.IntegerField()
    cenaB = models.FloatField()
    prtljagE = models.BooleanField()
    vremePolaska = models.TimeField()
    vremeDolaska = models.TimeField()
    
    
    


    


# Create your models here.
