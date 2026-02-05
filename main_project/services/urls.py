from django.urls import path
from .views import services_view
from . import views
urlpatterns = [
    path('', views.services_view, name='services'),
]