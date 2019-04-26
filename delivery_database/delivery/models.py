from django.db import models

# Create your models here.

class Driver(models.Model):
    user_id = models.AutoField(primary_key=True)
    SSN = models.Charfield(max_length=10)
    name = models.Charfield(max_length=50)
    email = models.Charfield(max_length=80)
    state = models.Charfield(max_length=80)
    city = models.Charfield(max_length=80)
    Company = models.Charfield(max_length=80)

class Vehicle(models.Model):
    models = models.Charfield(max_length=60)
    colors = models.Charfield(max_length=60)
    year = models.Charfield(max_length=60)

class Delivery(model.Model):
    amount = models.Integerfield()
    tip = models.Integerfield()
    driver = models.ForeignKey(
      Driver,
      related_name = 'deliveries',
      on_delete = models.CASCADE)
    vehicle = models.ForeignKey(
      Vehicle,
      related_name = 'deliveries',
      on_delete = models.CASCADE)
