from django.db import models

# Create your models here.

class Class(models.Model):
    stu_name = models.CharField(max_length=100)
    Father_name = models.CharField(max_length=100)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20)

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)


  