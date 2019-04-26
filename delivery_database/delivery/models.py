from django.db import models

# Create your models here.

class Driver(models.Model):
    STATE_CHOICES = [
      ('AL', 'Alabama'),
      ('AK', 'Alaska'),
      ('AZ', 'Arizona'),
      ('AR', 'Arkansa'),
      ('CA', 'California'),
      ('CO', 'Colorado'),
      ('CT', 'Connecticut'),
      ('DE', 'Delaware'),
      ('FL', 'Florida'),
      ('GA', 'Georgia'),
      ('HI', 'Hawaii'),
      ('ID', 'Idaho'),
      ('IL', 'Illinois'),
      ('IN', 'Indiana'),
      ('KS', 'Kansas'),
      ('KY', 'Kentucky'),
      ('LA', 'Lousianna'),
      ('ME', 'Maine'),
      ('MD', 'Maryland'),
      ('MA', 'Massachusetts'),
      ('MI', 'Michigan'),
      ('MN', 'Minnesota'),
      ('MS', 'Mississippi'),
      ('MO', 'Missouri'),
      ('MT', 'Montana'),
      ('NE', 'Nebraska'),
      ('NV', 'Nevada'),
      ('NH', 'New Hampshire'),
      ('NJ', 'New Jersey'),
      ('NM', 'New Mexico'),
      ('NY', 'New York'),
      ('NC', 'North Carolina'),
      ('ND', 'North Dakota'),
      ('OH', 'Ohio'),
      ('OR', 'Oregon'),
      ('PA', 'Pennsylvania'),
      ('RI', 'Rhode Island'),
      ('SC', 'South Carolina'),
      ('SD', 'South Dakota'),
      ('TN', 'Tennessee'),
      ('TX', 'Texas'),
      ('UT', 'Utah'),
      ('VT', 'Vermont'),
      ('VA', 'Virginia'),
      ('WA', 'Washington'),
      ('WV', 'West Virginia'),
      ('WI', 'Wisconsin'),
      ('WY', 'Wyoming')
    ]

    user_id = models.AutoField(primary_key=True)
    ssn = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    state = models.CharField(max_length=80, choices=STATE_CHOICES)
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

class Delivery(models.Model):
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
