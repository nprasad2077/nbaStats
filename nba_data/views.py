from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import PlayerData
from rest_framework import generics
from .serializers import PlayerDataSerializer


# Create your views here.

# API view to list all PlayerData instances
class PlayerDataList(generics.ListCreateAPIView):
    queryset = PlayerData.objects.all()
    serializer_class = PlayerDataSerializer
    # pagination_class = None
    
    
