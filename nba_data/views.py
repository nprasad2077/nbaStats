from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import PlayerData

# Create your views here.

def get_player_data(request):
    data = serializers.serialize('json', PlayerData.objects.all())
    return JsonResponse(data, safe=False)