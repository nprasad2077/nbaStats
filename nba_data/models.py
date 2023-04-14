from django.db import models

# Create your models here.
class PlayerData(models.Model):
    player = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    games_started = models.CharField(max_length=100)
    minutes_pg = models.CharField(max_length=100)
    field_goals = models.CharField(max_length=100)
    field_attempts = models.CharField(max_length=100)
    field_percent = models.CharField(max_length=100)
    three_fg = models.CharField(max_length=100)
    three_attempts = models.CharField(max_length=100)
    three_percent = models.CharField(max_length=100)
    two_fg = models.CharField(max_length=100)
    two_attempts = models.CharField(max_length=100)
    two_percent = models.CharField(max_length=100)
    effect_fg_percent = models.CharField(max_length=100)
    ft = models.CharField(max_length=100)
    fta = models.CharField(max_length=100)
    ft_percent = models.CharField(max_length=100)
    ORB= models.CharField(max_length=100)
    DRB = models.CharField(max_length=100)
    TRB = models.CharField(max_length=100)
    AST = models.CharField(max_length=100)
    STL = models.CharField(max_length=100)
    BLK = models.CharField(max_length=100)
    TOV = models.CharField(max_length=100)
    PF = models.CharField(max_length=100)
    PTS = models.CharField(max_length=100)
    
    def __str__(self):
        return self.player

