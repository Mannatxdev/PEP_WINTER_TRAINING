from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('complete/<int:pk>/', views.complete_task, name='complete_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('subtask/add/<int:pk>/', views.add_subtask, name='add_subtask'),
    path('subtask/toggle/<int:pk>/', views.toggle_subtask, name='toggle_subtask'),
    path('subtask/delete/<int:pk>/', views.delete_subtask, name='delete_subtask'),

]
