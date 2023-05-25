from django.contrib import admin
from .models import Event
from .models import UserRegistered

# Register your models here.
admin.site.register(Event)
admin.site.register(UserRegistered)
