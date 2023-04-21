from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import PlayerData
from rest_framework import generics
from .serializers import PlayerDataSerializer


# Create your views here.

# API view to list all PlayerData instances
class PlayerDataList(generics.ListCreateAPIView):
    queryset = PlayerData.objects.all().order_by('id')
    serializer_class = PlayerDataSerializer
    # pagination_class = None
    
    
# Fetch player data by team
class PlayerDataByTeamList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer
    
    def get_queryset(self):
        team = self.kwargs['team']
        return PlayerData.objects.filter(team=team)
    
    
# Fetch player data by season
class PlayerDataBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer
    
    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season)
    
    
# Fetch player data by player name
class PlayerDataByNameList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer
    
    def get_queryset(self):
        name = self.kwargs['name']
        return PlayerData.objects.filter(name__icontains=name)
