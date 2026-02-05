from django.urls import path
from .views import home_view
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
]