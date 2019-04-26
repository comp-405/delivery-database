from django.db import models

# Create your models here.

class Driver(models.Model):
    user_id = models.AutoField(primary_key=True)
    ssm = models.Charfield(max_length=10)
    name = models.Charfield(max_length=50)
    email = models.Charfield(max_length=80)
    state = models.Charfield(max_length=80)
    city = models.Charfield(max_length=80)
    company = models.Charfield(max_length=80)

    def __str__(self):
      return self.name

class Vehicle(models.Model):
    model = models.Charfield(max_length=60)
    color = models.Charfield(max_length=60)
    year = models.Charfield(max_length=60)

    def __str__(self):
      return f"{self.year} {self.model}"

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
    
    def __str__(self):
      return f"Total: {self.amount}, Tip: {self.tip}"
