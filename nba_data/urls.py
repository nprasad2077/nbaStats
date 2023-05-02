from django.urls import path
from .views import PlayerDataList, PlayerDataByTeamList, PlayerDataBySeasonList, PlayerDataByNameList, TopScorersbySeasonList, TopScorersbySeasonListPlayoffs, ThreeTwoTopPointTrends, TopAssistsBySeasonList, TopReboundsBySeasonList, TopBlocksBySeasonList, TopStealsBySeasonList, TopOffensiveReboundsBySeasonList, TopDefensiveReboundsBySeasonList, PointsPerGameHistogramBySeasonList, TopPtsScatterPlotData, TopPtsScatterPlotDataFast, TopPtsScatterPlotDataFast2018, Top20ScorersPost2009WS, Top20ScorersPost2014WS, Top20ScorersPost2018WS, TopAssistsBySeasonListPlayoffs, Top25ScorersPostSeasonPlayoffs, TopPtsScatterPlotDataFastSelect

urlpatterns = [
    path('api/playerdata/', PlayerDataList.as_view(), name='playerdata_list'),
    path('api/playerdata/team/<str:team>/', PlayerDataByTeamList.as_view(), name='playerdata_by_team'),
    path('api/playerdata/season/<str:season>/', PlayerDataBySeasonList.as_view(), name='playerdata_by_season'),
    path('api/playerdata/name/<str:name>/', PlayerDataByNameList.as_view(), name='playerdata_by_name'),
    path('api/playerdata/topscorers/season/<str:season>/', TopScorersbySeasonList.as_view(), name='top_scorers_by_season'),
    path('api/playerdata/topscorers/playoffs/<str:season>/', TopScorersbySeasonListPlayoffs.as_view(), name='top_scorers_by_season_playoffs'),
    path('api/three_two_point_trends/', ThreeTwoTopPointTrends.as_view(), name='three_two_point_trends'),
    path('api/top_assists/<int:season>/', TopAssistsBySeasonList.as_view(), name='top_assists'),
    path('api/top_assists/playoffs/<int:season>/', TopAssistsBySeasonListPlayoffs.as_view(), name='top_assists_playoffs'),
    path('api/top_rebounds/<int:season>/', TopReboundsBySeasonList.as_view(), name='top_rebounds'),
    path('api/top_blocks/<int:season>/', TopBlocksBySeasonList.as_view(), name='top_blocks'),
    path('api/top_steals/<int:season>/', TopStealsBySeasonList.as_view(), name='top_steals'),
    path('api/top_rebounds_offensive/<int:season>/', TopOffensiveReboundsBySeasonList.as_view(), name='top_rebounds_ORB'),
    path('api/top_rebounds_defensive/<int:season>/', TopDefensiveReboundsBySeasonList.as_view(), name='top_rebounds_DRB'),
    path('api/points_per_game_histogram/<int:season>/', PointsPerGameHistogramBySeasonList.as_view(), name='points_per_game_histogram'),
    path('api/top_pts_scatter_plot/', TopPtsScatterPlotData.as_view(), name='top_pts_scatter_plot'),
    path('api/top_pts_scatter_plot_fast/', TopPtsScatterPlotDataFast.as_view(), name='top_pts_scatter_plot_fast'),
    path('api/top_pts_scatter_plot_fast_2018/', TopPtsScatterPlotDataFast2018.as_view(), name='top_pts_scatter_plot_fast_2018'),
    path('api/top_20_post_2009_PTS_ws/', Top20ScorersPost2009WS.as_view(), name='top_20_post_2009_PTS_ws'),
    path('api/top_20_post_2014_PTS_ws/', Top20ScorersPost2014WS.as_view(), name='top_20_post_2014_PTS_ws'),
    path('api/top_20_post_2018_PTS_ws/', Top20ScorersPost2018WS.as_view(), name='top_20_post_2018_PTS_ws'),
    path('api/top_25_PTS_ws/playoffs/<int:season>/', Top25ScorersPostSeasonPlayoffs.as_view(), name='top_25_PTS_ws_playoffs'),
    path('api/top_25_PTS_ws/season/<int:season>/', TopPtsScatterPlotDataFastSelect.as_view(), name='top_25_PTS_ws_season'),
]