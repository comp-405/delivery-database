from django.views.generic import CreateView

from .models import Driver, Vehicle, Delivery

# Create your views here.

class DriverCreateView(CreateView):
    model = Driver
    template_name = 'driver_new.html'
    fields = '__all__'

class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = '__all__'

def select_user(request):
    pass

def select_vehicle(request, driver):
    pass

def create_delivery(request, driver, vehicle):
    pass