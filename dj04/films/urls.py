from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.film_list, name='film_list'),
    path('add/', views.film_create, name='film_create'),
    path('edit/<int:pk>/', views.film_update, name='film_update'),
    path('delete/<int:pk>/', views.film_delete, name='film_delete'),
]
