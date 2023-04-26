from django.urls import path
from .views import PlayerDataList, PlayerDataByTeamList, PlayerDataBySeasonList, PlayerDataByNameList, TopScorersbySeasonList, ThreeTwoTopPointTrends, TopAssistsBySeasonList, TopReboundsBySeasonList, TopBlocksBySeasonList, TopStealsBySeasonList, TopOffensiveReboundsBySeasonList, TopDefensiveReboundsBySeasonList

urlpatterns = [
    path('api/playerdata/', PlayerDataList.as_view(), name='playerdata_list'),
    path('api/playerdata/team/<str:team>/', PlayerDataByTeamList.as_view(), name='playerdata_by_team'),
    path('api/playerdata/season/<str:season>/', PlayerDataBySeasonList.as_view(), name='playerdata_by_season'),
    path('api/playerdata/name/<str:name>/', PlayerDataByNameList.as_view(), name='playerdata_by_name'),
    path('api/playerdata/topscorers/season/<str:season>/', TopScorersbySeasonList.as_view(), name='top_scorers_by_season'),
    path('api/three_two_point_trends/', ThreeTwoTopPointTrends.as_view(), name='three_two_point_trends'),
    path('api/top_assists/<int:season>/', TopAssistsBySeasonList.as_view(), name='top_assists'),
    path('api/top_rebounds/<int:season>/', TopReboundsBySeasonList.as_view(), name='top_rebounds'),
    path('api/top_blocks/<int:season>/', TopBlocksBySeasonList.as_view(), name='top_blocks'),
    path('api/top_steals/<int:season>/', TopStealsBySeasonList.as_view(), name='top_steals'),
    path('api/top_rebounds_offensive/<int:season>/', TopOffensiveReboundsBySeasonList.as_view(), name='top_rebounds_ORB'),
    path('api/top_rebounds_defensive/<int:season>/', TopDefensiveReboundsBySeasonList.as_view(), name='top_rebounds_DRB'),
]