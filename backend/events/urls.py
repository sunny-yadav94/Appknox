from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.getAllEvents, name='events'),
    path('events/new/', views.newEvent, name='new_event'),
    path('events/<str:pk>/', views.getEvent, name='event'),
    path('events/<str:pk>/update/', views.updateEvent, name='update_event'),
    path('events/<str:pk>/delete/', views.deleteEvent, name='delete_event'),
    path('events/<str:pk>/register/', views.registerEvent, name='register_event'),
    path('me/events/applied/', views.getCurrentUserRegisteredEvents, name='current_user_register_event'),
    path('events/<str:pk>/check/', views.isRegistered, name='is_registered_event'),
    path('events/<str:pk>/users/', views.getUserRegistered, name='get_users_registered'),
]