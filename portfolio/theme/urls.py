from django.urls import path
from . import views
urlpatterns = [
    path('tailwind',views.home,name='home')
]
