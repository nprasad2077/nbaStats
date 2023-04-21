from django.urls import path
from .views import PlayerDataList

urlpatterns = [
    path('api/playerdata/', PlayerDataList.as_view(), name='playerdata_list'),
]