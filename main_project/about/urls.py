from django.urls import path
from .views import about_view
from . import views

urlpatterns = [
    path('', views.about_view, name='about'),
]