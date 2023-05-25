from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from django.contrib.auth import authenticate, login, logout
# from account.models import adminRegister
from rest_framework.generics import GenericAPIView
from .serializers import*
from .serializers import SignUpSerializer, UserSerializer
from django.contrib.auth.hashers import make_password

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
import random
import requests
from django.shortcuts import get_object_or_404



# register admin with password(not used in frontend)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    data = request.data

    user = SignUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                username = data['email'],
                password = make_password(data['password']),
            )

            return Response({
                'message': 'User Registered.'},
                status=status.HTTP_200_OK
            )

        else:
            return Response({
                'error': 'User Already Exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

    else:
        return Response(user.errors) 
    

# details of all registered users

@api_view(['GET'])
@permission_classes([IsAdminUser])
def allUser(request): 

    users = User.objects.all().order_by('user_id')

    number = User.objects.all().count()


    serializer = UserSerializer(users, many=True)
    # print(serializer.data)

    return Response({
        "totalUser":number,
        'allUser':serializer.data
        }) 

 

# details of logged in candidate

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request): 

    user = UserSerializer(request.user)

    return Response(user.data) 












    


    





   
   



