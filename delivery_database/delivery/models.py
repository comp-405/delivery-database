from django.db import models

# Create your models here.

class Driver(models.Model):
    user_id = models.AutoField(primary_key=True)
    ssm = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    company = models.CharField(max_length=80)

    def __str__(self):
      return self.name

class Vehicle(models.Model):
    model = models.CharField(max_length=60)
    color = models.CharField(max_length=60)
    year = models.CharField(max_length=60)

    def __str__(self):
      return f"{self.year} {self.model}"

class Delivery(model.Model):
    amount = models.IntegerField()
    tip = models.IntegerField()
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
