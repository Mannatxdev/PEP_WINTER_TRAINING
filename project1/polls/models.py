
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
        last_modified = models.DateTimeField(auto_now_add = True)
        img = models.ImageField(upload_to= "images/")


        # renames the instances of  the model
        # with their title name
    def __str__(self):
        return self.title
