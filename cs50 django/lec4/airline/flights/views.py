from django.shortcuts import render
from . models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    
    context={
        "flights":Flight.objects.all()
    }
    
    return render(request, "flights/index.html",  context)

def flight(request, flight_id):
    flight=Flight.objects.get(pk=flight_id) #primary key = flightid
    return render (request, "flights/flight.html", {
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })
    
def book(request, flight_id):
    if request.method == 'POST':
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
     