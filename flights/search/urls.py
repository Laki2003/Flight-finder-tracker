from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name= 'index'),
        path('addFlight/', views.create_flight, name = 'createFlight'),
        path('createFlightPost/', views.create_flight_post, name="createFlightPost")
       

]