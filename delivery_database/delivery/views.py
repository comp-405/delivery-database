from django.views.generic import CreateView
from django.shortcuts import render

from .forms import DeliveryForm
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
    all_drivers = Driver.objects.all().order_by('name')
    return render(request, 'select_driver.html', {'all_drivers': all_drivers})

def select_vehicle(request, driver):
    all_vehicles = Vehicle.objects.all().order_by('year')
    return render(request, 'select_vehicle.html', {'all_vehicles': all_vehicles, 'driver': driver})

def create_delivery(request, driver, vehicle):
    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        if delivery_form.is_valid():
            new_delivery = delivery_form.save(commit=False)
            driver = Driver.objects.get(user_id=driver)
            vehicle = Vehicle.objects.get(id=vehicle)
            new_delivery.driver = driver
            new_delivery.vehicle = vehicle
            new_delivery.save()
            return render(request, 'delivery_done.html', {'new_delivery': new_delivery})
    else:
        delivery_form = DeliveryForm()
        return render(request, 'delivery_new.html', {'delivery_form': delivery_form})