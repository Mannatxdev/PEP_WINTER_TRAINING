
from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # address  = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} < {self.email} >"
    

class FormModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # last_modified = models.DateTimeField(auto_now_add = True)
    # img = models.ImageField(upload_to= "images/")


        # renames the instances of  the model
        # with their title name
    def __str__(self):
        return self.title

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.hashers import identify_hasher

class LoginUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password : str)-> None:
        self.password = make_password(raw_password)

    def check_password(self, raw_password : str) -> bool:
        return check_password(raw_password, self.password)
    
    
    # def check_password(self, raw_password : str) -> bool:
    #     return self.password == make_password(raw_password)
    
    def save(self, *args, **kwargs):
        try:
            identify_hasher(self.password)
        except ValueError:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    