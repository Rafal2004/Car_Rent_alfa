from operator import mod
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Body_Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car_Brand(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Gearbox(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Car_Model(models.Model):
    brand = models.ForeignKey(Car_Brand, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="car", null=True)
    title = models.CharField(max_length=100, default=None)
    brand = models.ForeignKey(
        Car_Brand, on_delete=models.CASCADE, related_name='brand', null=True)
    model = models.ForeignKey(
        Car_Model, on_delete=models.CASCADE, related_name='model', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    body_type = models.ForeignKey(
        Body_Type, on_delete=models.CASCADE, related_name='body_type', null=True)
    year = models.IntegerField(default=None)
    gearbox = models.ForeignKey(
        Gearbox, on_delete=models.CASCADE, related_name='gearbox', null=True)
    mileage = models.IntegerField(null=True)
    contact_email = models.EmailField(max_length=254, default=None)
    contact_phone_number = models.IntegerField(default=None)
    description = models.TextField(default=None)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title



