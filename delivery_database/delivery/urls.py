from django.urls import path

from .views import (
  home,
  DriverCreateView,
  VehicleCreateView,
  select_driver,
  select_vehicle,
  create_delivery
)

urlpatterns = [
    path('', home, name='home'),
    path('new-delivery/', select_driver, name='select_driver'),
    path('new-delivery/<int:driver>/', select_vehicle, name='select_vehicle'),
    path('new-delivery/<int:driver>/<int:vehicle>/', create_delivery, name='create_delivery'),
    path('new-driver/', DriverCreateView.as_view(), name='new_driver'),
    path('new-vehicle/<int:driver>/', VehicleCreateView.as_view(), name='new_vehicle'),
]
