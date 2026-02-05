from django.db import models

# Create your models here.
class user:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # phone_num = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name}{self.last_name} < {self.email} > "
