from django.db import models

class Car(models.Model):
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  year = models.IntegerField()
  daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.CharField(max_length=20, choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Truck', 'Truck')])
  is_available = models.BooleanField(default=True)

class Rental(models.Model):
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  customer_name = models.CharField(max_length=100)
  rental_start_date = models.DateField()
  rental_end_date = models.DateField()
