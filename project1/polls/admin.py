from django.contrib import admin

# Register your models here.
from .models import LoginUser, user
admin.site.register(user)

from .models import FormModel
admin.site.register(LoginUser)
admin.site.register(FormModel)