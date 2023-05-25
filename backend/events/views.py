from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer, UserRegisteredSerializer
from .models import Event, UserRegistered
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.utils import timezone


# list all events posted by admin

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllEvents(request):

    events = Event.objects.all().order_by('-id')

    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)



# summary of a particular event

@api_view(['GET'])
@permission_classes([AllowAny])
def getEvent(request, pk):

    event = get_object_or_404(Event, id=pk)

    serializer = EventSerializer(event, many=False)

    return Response(serializer.data) 



# post a new event by admin

@api_view(['POST'])
@permission_classes([IsAdminUser])
def newEvent(request):

        data = request.data

        event = Event.objects.create(**data)

        serializer = EventSerializer(event, many=False)


        return Response(serializer.data) 



# update already posted event by admin

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateEvent(request, pk):

    event = get_object_or_404(Event, id=pk)

    event.title = request.data['title']
    event.maxSeat = request.data['maxSeat']
    event.mode = request.data['mode']
    event.location = request.data['location']
    event.startDate = request.data['startDate']
    event.endDate = request.data['endDate']

    event.save()

    serializer = EventSerializer(event, many=False)

    return Response(serializer.data)



# delete event posted by admin

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteEvent(request,pk):

    event = get_object_or_404(Event, id=pk)

    event.delete()

    return Response({ 'message': 'Event is Deleted.' }, status=status.HTTP_200_OK)



# process for user to register an event

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerEvent(request,pk):

    user = request.user
    event = get_object_or_404(Event, id=pk)
    registeredOn = timezone.now()
    availableSeat = event.availableSeat
    seatBooked = request.data['seatBooked']
    

    if event.endDate < timezone.now() or event.startDate > timezone.now():
        return Response({'error':'You cannot register this event as window is closed'}, status=status.HTTP_400_BAD_REQUEST) 
    

    alreadyRegistered = event.userregistered_set.filter(user=user).exists()

    if alreadyRegistered:
         return Response({'error':'you have already registered this event.'}, status=status.HTTP_400_BAD_REQUEST) 

    eventRegistered = UserRegistered.objects.create(
        event = event,
        user = user,
        registeredOn = registeredOn,
        seatBooked = seatBooked,
    ) 

    print(availableSeat)
    print(seatBooked)  

    event.availableSeat = availableSeat-int(seatBooked)

    event.save()

    return Response({
        'applied':True,
        'event_id':eventRegistered.id,
    },
    status=status.HTTP_200_OK
    )        


# list of events registered by user 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUserRegisteredEvents(request):

    args = { 'user_id': request.user.id }

    events = UserRegistered.objects.filter(**args).order_by('-registeredOn')

    serializer = UserRegisteredSerializer(events, many=True)

    return Response(serializer.data)  



# user's event register button(if registered or not)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def isRegistered(request, pk):

    user = request.user
    event = get_object_or_404(Event, id=pk)

    applied = event.userregistered_set.filter(user=user).exists()
    return Response(applied)  



# list of users that has registered for the events in admin dashboard

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserRegistered(request, pk):

    args = { 'event_id': pk }

    users = UserRegistered.objects.filter(**args)

    serializer = UserRegisteredSerializer(users, many=True)

    return Response(serializer.data) 





