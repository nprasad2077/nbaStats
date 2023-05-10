# Serializers are defined that will convert model instances to JSON
from rest_framework import serializers
from .models import PlayerData, PlayerTotalsData, PlayerAdvancedData, PlayerPlayoffTotalsData, PlayerPlayoffAdvancedData, PlayerSalaryData, PlayerShotChartData

class PlayerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerData
        fields = '__all__'
        
class HistogramDataSerializer(serializers.Serializer):
    range = serializers.CharField()
    count = serializers.IntegerField()
    
class PlayerPlayoffTotalsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPlayoffTotalsData
        fields = '__all__'

class PlayerTotalsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerTotalsData
        fields = '__all__'

class PlayerAdvancedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerAdvancedData
        fields = '__all__'

class PlayerPlayoffAdvancedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPlayoffAdvancedData
        fields = '__all__'

class PlayerSalaryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSalaryData
        fields = '__all__'

class PlayerShotChartDataSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()
    
    class Meta:
        model = PlayerShotChartData
        fields = ['top', 'left', 'date', 'qtr', 'time_remaining', 'result', 'shot_type', 'distance_ft', 'lead', 'lebron_team_score', 'opponent_team_score', 'opponent', 'team', 'season', 'color']
        
    def get_color(self, obj):
        return 'green' if obj.result else 'red'
        

