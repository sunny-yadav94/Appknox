from django.urls import path
from . import views
from .views import*

urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', views.allUser, name='all_user'),
    path('me/', views.currentUser, name='current_user'),
]