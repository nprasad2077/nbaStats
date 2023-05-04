from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.core import serializers
from .models import PlayerData, PlayerTotalsData, PlayerAdvancedData, PlayerPlayoffTotalsData, PlayerPlayoffAdvancedData
from rest_framework import generics
from .serializers import PlayerDataSerializer, HistogramDataSerializer, PlayerPlayoffTotalsDataSerializer, PlayerTotalsDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Sum, F, FloatField, Min, Max
from collections import Counter
import math
from django.db import connection


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

# Fetch Top 20 players by total PTS for season.
class TopScorersbySeasonTotalsList(generics.ListAPIView):
    serializer_class = PlayerTotalsDataSerializer
    
    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerTotalsData.objects.filter(season=season).order_by('-PTS')[:20]


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
    
# Fetch Top 20 players by AST totals DESC for the season

class TopAssistsBySeasonTotalsList(generics.ListAPIView):
    serializer_class = PlayerPlayoffTotalsDataSerializer
    
    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerTotalsData.objects.filter(season=season).order_by('-AST')[:20]
    

# Fetch Top 20 players by TRB DESC for season specified.


class TopReboundsBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-TRB')[:20]
    
# Fetch top 20 players by TRB Totals for season.

class TopReboundsbySeasonTotalsList(generics.ListAPIView):
    serializer_class = PlayerTotalsDataSerializer
    
    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerTotalsData.objects.filter(season=season).order_by('-TRB')[:20]
    
    

# Fetch Top 20 players by BLK DESC for specified season.


class TopBlocksBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-BLK')[:20]



# Fetch Top 20 players by BLK totals DESC for specified season.

class TopBlocksbySeasonTotalsList(generics.ListAPIView):
    serializer_class = PlayerTotalsDataSerializer
    
    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerTotalsData.objects.filter(season=season).order_by('-BLK')[:20]
    

# Fetch Top 20 players by STL DESC for season specified.


class TopStealsBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-STL')[:20]

# Fetch Top 20 players by STL totals DESC for season specified.

class TopStealsbySeasonTotalsList(generics.ListAPIView):
    serializer_class = PlayerTotalsDataSerializer
    
    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerTotalsData.objects.filter(season=season).order_by('-STL')[:20]
    

# Fetch Top 20 players by ORB DESC for season.


class TopOffensiveReboundsBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-ORB')[:20]
    
# Fetch Top 20 players by ORB totals DESC for season.

class TopOffensiveReboundsbySeasonTotalsList(generics.ListAPIView):
    serializer_class = PlayerTotalsDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerTotalsData.objects.filter(season=season).order_by('-ORB')[:20]


# Fetch Top 20 players by DRB DESC for season.

class TopDefensiveReboundsBySeasonList(generics.ListAPIView):
    serializer_class = PlayerDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerData.objects.filter(season=season).order_by('-DRB')[:20]

# Fetch Top 20 players by DRB totals DESC for season.

class TopDefensiveReboundsBySeasonTotalsList(generics.ListAPIView):
    serializer_class = PlayerTotalsDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerTotalsData.objects.filter(season=season).order_by('-DRB')[:20]

# PTS Histogram


class PointsPerGameHistogramBySeasonList(generics.ListAPIView):
    serializer_class = HistogramDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        queryset = PlayerData.objects.filter(season=season)

        # Get the points per game for each player
        points_per_game_list = [float(player.PTS) for player in queryset]

        # Define histogram bins (e.g., 0-5, 5-10, 10-15, etc.)
        bin_ranges = range(0, int(math.ceil(max(points_per_game_list))) + 1, 5)
        histogram_data = Counter()

        # Fill the histogram with data
        for ppg in points_per_game_list:
            bin_index = next(
                (i for i, r in enumerate(bin_ranges) if r >= ppg), -1)
            if bin_index >= 1:
                bin_label = f"{bin_ranges[bin_index - 1]}-{bin_ranges[bin_index]}"
                histogram_data[bin_label] += 1

        # Convert histogram_data to list of dicts for serialization
        histogram_list = [{"range": k, "count": v}
                          for k, v in histogram_data.items()]

        return histogram_list


# Scatter Plot - Top 30 players by total PTS across all seasons in DB. Then map those 30 players on a scatter plot against total PTS/WS for each season.

class TopPtsScatterPlotData(APIView):
    def get(self, request, *args, **kwargs):
        # Get the top 25 players by overall PTS
        top_players = PlayerTotalsData.objects.values('player_name') \
            .annotate(total_pts=Sum(F('PTS'))) \
            .order_by('-total_pts')[:25]

        # Get the PTS and WS for the corresponding seasons of the top 25 players
        data = []
        for player in top_players:
            player_name = player['player_name']
            player_seasons = PlayerTotalsData.objects.filter(player_name=player_name) \
                .values('season') \
                .annotate(total_pts=Sum(F('PTS'))) \
                .order_by('season')

            # Combine the WS data from PlayerAdvancedData
            for season in player_seasons:
                season_ws = PlayerAdvancedData.objects.filter(player_name=player_name, season=season['season']) \
                    .aggregate(total_ws=Sum('ws'))
                season['total_ws'] = season_ws['total_ws']

            data.append({
                'player_name': player_name,
                'seasons': list(player_seasons)
            })

        return Response(data)
    
# change lines 223, 227, and 233 where the comments are to alter seasons returned.
class TopPtsScatterPlotDataFast(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                -- The modified query from earlier
                WITH player_season_pts AS (
                  SELECT player_name, season, SUM("PTS") as season_pts
                  FROM nba_data_playertotalsdata
                  WHERE player_name IN (SELECT player_name FROM (
                                           SELECT player_name, SUM("PTS") as total_pts
                                           FROM nba_data_playertotalsdata
                                           -- WHERE season >= 2021
                                           GROUP BY player_name
                                           ORDER BY total_pts DESC
                                           LIMIT 25) as top_25_players)
                  -- AND season >= 2021               
                  GROUP BY player_name, season
                ),
                player_season_ws AS (
                  SELECT player_name, season, SUM("ws") as season_ws
                  FROM nba_data_playeradvanceddata
                  -- WHERE season >= 2021
                  GROUP BY player_name, season
                )
                SELECT player_season_pts.player_name, player_season_pts.season, player_season_pts.season_pts, player_season_ws.season_ws
                FROM player_season_pts
                JOIN player_season_ws
                ON player_season_pts.player_name = player_season_ws.player_name AND player_season_pts.season = player_season_ws.season
                ORDER BY player_season_pts.player_name, player_season_pts.season;
            """)
            rows = cursor.fetchall()

        result = []
        for row in rows:
            player_name, season, season_pts, season_ws = row
            result.append({
                'player_name': player_name,
                'season': season,
                'season_pts': season_pts,
                'season_ws': season_ws
            })

        return Response(result)
    

class TopPtsScatterPlotDataFast2018(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                -- The modified query from earlier
                WITH player_season_pts AS (
                  SELECT player_name, season, SUM("PTS") as season_pts
                  FROM nba_data_playertotalsdata
                  WHERE player_name IN (SELECT player_name FROM (
                                           SELECT player_name, SUM("PTS") as total_pts
                                           FROM nba_data_playertotalsdata
                                           WHERE season >= 2018
                                           GROUP BY player_name
                                           ORDER BY total_pts DESC
                                           LIMIT 25) as top_25_players)
                  AND season >= 2018               
                  GROUP BY player_name, season
                ),
                player_season_ws AS (
                  SELECT player_name, season, SUM("ws") as season_ws
                  FROM nba_data_playeradvanceddata
                  WHERE season >= 2018
                  GROUP BY player_name, season
                )
                SELECT player_season_pts.player_name, player_season_pts.season, player_season_pts.season_pts, player_season_ws.season_ws
                FROM player_season_pts
                JOIN player_season_ws
                ON player_season_pts.player_name = player_season_ws.player_name AND player_season_pts.season = player_season_ws.season
                ORDER BY player_season_pts.player_name, player_season_pts.season;
            """)
            rows = cursor.fetchall()

        result = []
        for row in rows:
            player_name, season, season_pts, season_ws = row
            result.append({
                'player_name': player_name,
                'season': season,
                'season_pts': season_pts,
                'season_ws': season_ws
            })

        return Response(result)

class TopPtsScatterPlotDataFastSelect(APIView):
    def get(self, request, season):
        with connection.cursor() as cursor:
            cursor.execute("""
                WITH player_season_pts AS (
                  SELECT player_name, season, SUM("PTS") as season_pts
                  FROM nba_data_playertotalsdata
                  WHERE player_name IN (SELECT player_name FROM (
                                           SELECT player_name, SUM("PTS") as total_pts
                                           FROM nba_data_playertotalsdata
                                           WHERE season >= %s
                                           GROUP BY player_name
                                           ORDER BY total_pts DESC
                                           LIMIT 25) as top_25_players)
                  AND season >= %s
                  GROUP BY player_name, season
                ),
                player_season_ws AS (
                  SELECT player_name, season, SUM("ws") as season_ws
                  FROM nba_data_playeradvanceddata
                  WHERE season >= %s
                  GROUP BY player_name, season
                )
                SELECT player_season_pts.player_name, player_season_pts.season, player_season_pts.season_pts, player_season_ws.season_ws
                FROM player_season_pts
                JOIN player_season_ws
                ON player_season_pts.player_name = player_season_ws.player_name AND player_season_pts.season = player_season_ws.season
                ORDER BY player_season_pts.player_name, player_season_pts.season;
            """, (season, season, season))
            rows = cursor.fetchall()

        result = []
        for row in rows:
            player_name, season, season_pts, season_ws = row
            result.append({
                'player_name': player_name,
                'season': season,
                'season_pts': season_pts,
                'season_ws': season_ws
            })

        return Response(result)

    
    
# Top 20 players in playoffs by PTS X ws for scatter plot in chart.js
    
class Top20ScorersPost2009WS(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                WITH player_playoff_pts AS (
                  SELECT player_name, season, SUM("PTS") as season_pts
                  FROM nba_data_playerplayofftotalsdata
                  WHERE player_name IN (SELECT player_name FROM (
                                               SELECT player_name, SUM("PTS") as total_pts
                                               FROM nba_data_playerplayofftotalsdata
                                               WHERE season >= 2010
                                               GROUP BY player_name
                                               ORDER BY total_pts DESC
                                               LIMIT 25) as top_25_players)
                  AND season >= 2010               
                  GROUP BY player_name, season
                ),
                player_playoff_ws AS (
                  SELECT player_name, season, SUM("ws") as season_ws
                  FROM nba_data_playerplayoffadvanceddata
                  WHERE season >= 2010
                  GROUP BY player_name, season
                )
                SELECT player_playoff_pts.player_name, player_playoff_pts.season, player_playoff_pts.season_pts, player_playoff_ws.season_ws
                FROM player_playoff_pts
                JOIN player_playoff_ws
                ON player_playoff_pts.player_name = player_playoff_ws.player_name AND player_playoff_pts.season = player_playoff_ws.season
                ORDER BY player_playoff_pts.player_name, player_playoff_pts.season;
            """)
            rows = cursor.fetchall()

        result = []
        for row in rows:
            player_name, season, season_pts, season_ws = row
            result.append({
                'player_name': player_name,
                'season': season,
                'season_pts': season_pts,
                'season_ws': season_ws
            })

        return Response(result)
    

class Top20ScorersPost2014WS(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                WITH player_playoff_pts AS (
                  SELECT player_name, season, SUM("PTS") as season_pts
                  FROM nba_data_playerplayofftotalsdata
                  WHERE player_name IN (SELECT player_name FROM (
                                               SELECT player_name, SUM("PTS") as total_pts
                                               FROM nba_data_playerplayofftotalsdata
                                               WHERE season >= 2015
                                               GROUP BY player_name
                                               ORDER BY total_pts DESC
                                               LIMIT 25) as top_25_players)
                  AND season >= 2015               
                  GROUP BY player_name, season
                ),
                player_playoff_ws AS (
                  SELECT player_name, season, SUM("ws") as season_ws
                  FROM nba_data_playerplayoffadvanceddata
                  WHERE season >= 2015
                  GROUP BY player_name, season
                )
                SELECT player_playoff_pts.player_name, player_playoff_pts.season, player_playoff_pts.season_pts, player_playoff_ws.season_ws
                FROM player_playoff_pts
                JOIN player_playoff_ws
                ON player_playoff_pts.player_name = player_playoff_ws.player_name AND player_playoff_pts.season = player_playoff_ws.season
                ORDER BY player_playoff_pts.player_name, player_playoff_pts.season;
            """)
            rows = cursor.fetchall()

        result = []
        for row in rows:
            player_name, season, season_pts, season_ws = row
            result.append({
                'player_name': player_name,
                'season': season,
                'season_pts': season_pts,
                'season_ws': season_ws
            })

        return Response(result)

class Top20ScorersPost2018WS(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                WITH player_playoff_pts AS (
                  SELECT player_name, season, SUM("PTS") as season_pts
                  FROM nba_data_playerplayofftotalsdata
                  WHERE player_name IN (SELECT player_name FROM (
                                               SELECT player_name, SUM("PTS") as total_pts
                                               FROM nba_data_playerplayofftotalsdata
                                               WHERE season >= 2019
                                               GROUP BY player_name
                                               ORDER BY total_pts DESC
                                               LIMIT 25) as top_25_players)
                  AND season >= 2019               
                  GROUP BY player_name, season
                ),
                player_playoff_ws AS (
                  SELECT player_name, season, SUM("ws") as season_ws
                  FROM nba_data_playerplayoffadvanceddata
                  WHERE season >= 2019
                  GROUP BY player_name, season
                )
                SELECT player_playoff_pts.player_name, player_playoff_pts.season, player_playoff_pts.season_pts, player_playoff_ws.season_ws
                FROM player_playoff_pts
                JOIN player_playoff_ws
                ON player_playoff_pts.player_name = player_playoff_ws.player_name AND player_playoff_pts.season = player_playoff_ws.season
                ORDER BY player_playoff_pts.player_name, player_playoff_pts.season;
            """)
            rows = cursor.fetchall()

        result = []
        for row in rows:
            player_name, season, season_pts, season_ws = row
            result.append({
                'player_name': player_name,
                'season': season,
                'season_pts': season_pts,
                'season_ws': season_ws
            })

        return Response(result)

class Top25ScorersPostSeasonPlayoffs(APIView):
    def get(self, request, season):
        try:
            season = int(season)
        except ValueError:
            raise Http404("Invalid season format.")

        with connection.cursor() as cursor:
            cursor.execute("""
                WITH player_playoff_pts AS (
                  SELECT player_name, season, SUM("PTS") as season_pts
                  FROM nba_data_playerplayofftotalsdata
                  WHERE player_name IN (SELECT player_name FROM (
                                               SELECT player_name, SUM("PTS") as total_pts
                                               FROM nba_data_playerplayofftotalsdata
                                               WHERE season >= %s
                                               GROUP BY player_name
                                               ORDER BY total_pts DESC
                                               LIMIT 25) as top_25_players)
                  AND season >= %s               
                  GROUP BY player_name, season
                ),
                player_playoff_ws AS (
                  SELECT player_name, season, SUM("ws") as season_ws
                  FROM nba_data_playerplayoffadvanceddata
                  WHERE season >= %s
                  GROUP BY player_name, season
                )
                SELECT player_playoff_pts.player_name, player_playoff_pts.season, player_playoff_pts.season_pts, player_playoff_ws.season_ws
                FROM player_playoff_pts
                JOIN player_playoff_ws
                ON player_playoff_pts.player_name = player_playoff_ws.player_name AND player_playoff_pts.season = player_playoff_ws.season
                ORDER BY player_playoff_pts.player_name, player_playoff_pts.season;
            """, (season, season, season))
            rows = cursor.fetchall()

        result = []
        for row in rows:
            player_name, season, season_pts, season_ws = row
            result.append({
                'player_name': player_name,
                'season': season,
                'season_pts': season_pts,
                'season_ws': season_ws
            })

        return Response(result)

    

class TopScorersbySeasonListPlayoffs(generics.ListAPIView):
    serializer_class = PlayerPlayoffTotalsDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerPlayoffTotalsData.objects.filter(season=season).order_by('-PTS')[:20]
    

class TopAssistsBySeasonListPlayoffs(generics.ListAPIView):
    serializer_class = PlayerPlayoffTotalsDataSerializer

    def get_queryset(self):
        season = self.kwargs['season']
        return PlayerPlayoffTotalsData.objects.filter(season=season).order_by('-AST')[:20]
    

class OverallDBStats(APIView):
    def get(self, request):
        total_players_regular = PlayerTotalsData.objects.count()
        total_players_playoffs = PlayerPlayoffAdvancedData.objects.count()
        regular_season_range = PlayerTotalsData.objects.aggregate(Min('season'), Max('season'))
        playoffs_season_range = PlayerPlayoffAdvancedData.objects.aggregate(Min('season'), Max('season'))
        
        response_data = {
            'total_players_regular': total_players_regular,
            'total_players_playoffs': total_players_playoffs,
            'regular_season_range': regular_season_range,
            'playoffs_season_range': playoffs_season_range,
        }

        return Response(response_data)




