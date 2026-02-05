from django.urls import path
from . import views
from .views import  home_view, form_view
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home_view, name = "home"),
    path("form", form_view,name= "form_view")
]