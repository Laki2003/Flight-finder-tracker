from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('pilot', views.pilot, name='pilot'),
    path('control', views.control, name="control")
]