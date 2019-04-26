from django.views.generic import CreateView

from .models import Driver, Vehicle, Delivery

# Create your views here.

class DriverCreateView(CreateView):
    model = Driver
    template_name = 'driver_new.html'
    fields = '__all__'