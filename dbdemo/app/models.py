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



### something random ###

class UNI(models.Model):
    student_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    sem = models.IntegerField()
    section = models.CharField(max_length=10)

class student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20)
    gmail = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    student_father_name = models.CharField(max_length=100)
    student_mother_name = models.CharField(max_length=100)
    student_address = models.CharField(max_length=200)

