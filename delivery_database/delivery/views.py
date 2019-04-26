from django.views.generic import CreateView
from django.shortcuts import render

from .models import Driver, Vehicle, Delivery

# Create your views here.

def home(request):
    return render(request, 'home.html')

class DriverCreateView(CreateView):
    model = Driver
    template_name = 'driver_new.html'
    fields = '__all__'

class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = '__all__'

def select_driver(request):
    return render(request, 'select_driver.html')

def select_vehicle(request, driver):
    return render(request, 'select_vehicle.html')

def create_delivery(request, driver, vehicle):
    pass