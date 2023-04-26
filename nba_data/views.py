from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import PlayerData
from rest_framework import generics
from .serializers import PlayerDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg


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


# Fetch Top 20 players by PTS DESC for the season specified.
class TopScorersbySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-PTS')[:20]


# Fetch and calculate the average 3P made, 3P attemps, 2P made, 2P attempts for all players in each season.
# Will use APIview here instead of generics.ListAPIView to avoid having to create a serializer to generate the queryset. avg_three_made and avg_two_made are new data points at the time of creation when compared to the per_game model.
class ThreeTwoTopPointTrends(APIView):
    def get(self, request, format=None):
        seasons = PlayerData.objects.values_list(
            'season', flat=True).distinct().order_by('season')
        data = []

        for season in seasons:
            season_data = PlayerData.objects.filter(season=season)
            avg_three_made = season_data.aggregate(Avg('three_fg'))[
                'three_fg__avg']
            avg_three_attempts = season_data.aggregate(Avg('three_attempts'))[
                'three_attempts__avg']
            avg_two_made = season_data.aggregate(Avg('two_fg'))['two_fg__avg']
            avg_two_attempts = season_data.aggregate(Avg('two_attempts'))[
                'two_attempts__avg']

            data.append({
                'season': season,
                'avg_three_made': avg_three_made,
                'avg_three_attempts': avg_three_attempts,
                'avg_two_made': avg_two_made,
                'avg_two_attempts': avg_two_attempts,
            })

        return Response(data)

# Fetch Top 20 players by AST DESC for season specified.


class TopAssistsBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-AST')[:20]

# Fetch Top 20 players by TRB DESC for season specified.


class TopReboundsBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-TRB')[:20]

# Fetch Top 20 players by BLK DESC for specified season.


class TopBlocksBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-BLK')[:20]

# Fetch Top 20 players by STL DESC for season specified.


class TopStealsBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-STL')[:20]
