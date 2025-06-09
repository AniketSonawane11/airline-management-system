from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.
def index(request):

    context = {
        "flights": Flight.objects.all()
    }

    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passenger": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context)
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args = (flight_id,)))




