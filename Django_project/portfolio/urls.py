# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('about/', views.about),
#     path('projects/', views.project),
#     path('resume/', views.resume),
#     path('contact/', views.contact),
#     path('register/', views.register, name='register'),
#     path('users/', views.user_list, name='user_list'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login_view, name='login'),
]