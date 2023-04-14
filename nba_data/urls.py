from django.urls import path
from .views import get_player_data

urlpatterns = [
    path('api/player_data/', get_player_data, name='player_data')
]