from rest_framework import serializers
from .models import Event, UserRegistered

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields ='__all__'

class UserRegisteredSerializer(serializers.ModelSerializer):

    event = EventSerializer()

    class Meta:
        model = UserRegistered
        fields ='__all__'
  
        
            