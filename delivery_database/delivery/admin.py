from django.contrib import admin

from .models import Driver, Vehicle, Delivery

# Register your models here.
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'ssn', 'name', 'state', 'company']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['model', 'color', 'year']

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['amount', 'tip', 'driver', 'vehicle']