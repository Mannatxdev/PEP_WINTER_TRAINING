from django.urls import path
from . import views
from .views import home_view, form_view, login_view, signup_view

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", home_view, name="home"),
    path("form/", form_view, name="form_view"),
    path("login/", login_view, name="login"),
    path("sign_up/", signup_view, name="signup"),
]