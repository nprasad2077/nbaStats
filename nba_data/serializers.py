# Serializers are defined that will convert model instances to JSON
from rest_framework import serializers
from .models import PlayerData

class PlayerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerData
        fields = '__all__'
        
class HistogramDataSerializer(serializers.Serializer):
    range = serializers.CharField()
    count = serializers.IntegerField()

