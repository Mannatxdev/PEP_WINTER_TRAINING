from django.contrib import admin

# Register your models here.
from .models import Car, Driver, Class, UNI, student

admin.site.register(Car)
admin.site.register(Driver) 
admin.site.register(Class)
admin.site.register(UNI)
admin.site.register(student)

