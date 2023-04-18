from django.db import models

# Create your models here.
class PlayerData(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    minutes_pg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_goals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    three_fg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    two_fg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    effect_fg_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    ft = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fta = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ft_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    ORB= models.DecimalField(max_digits=5, decimal_places=2, null=True)
    DRB = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TRB = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    AST = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    STL = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    BLK = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TOV = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PF = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PTS = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

