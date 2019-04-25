from django.db import models

# Create your models here.

class driver(models.Model):
    user_id = models.AutoField(prinmary_key=true)
    SSN = models.Charfield(max_length=10)
    name = models.Charfield(max_length = 50)
    email = models.Charfield(max_length = 80)
    state = models.Charfield(max_length = 80)
    city = models.Charfield(max_length = 80)
    Company = models.Charfield(max_length = 80)

class vehicles(models.Model):
    models = models.charfield(max_length = 60)
    colors = models.Charfield(max_length = 60)
    year = models.Charfield(max_length = 60)

class delivery(model.Model):
    amount = models.interfield()
    tip = models.interfield()
    driver = models.ForeignKey(driver.related_name = 'delivery', on_delete = models.CASCADE)
    vehicle = models.ForeignKey(vehicle.related_name = 'delivery', on_delete = models.CASCADE)
