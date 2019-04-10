from django.db import models

class CarTransaction(models.Model):
    car_id = models.IntegerField()
    import_country = models.CharField(max_length=80)
    car_model = models.CharField(max_length=20, blank=True)
    make = models.CharField(max_length=50, blank=True)
    sold_by = models.CharField(max_length=80, blank=True)
    sale_price = models.IntegerField(blank=True)

class Country(models.Model):
    country = models.CharField(max_length=80)
