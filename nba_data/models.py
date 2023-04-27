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
    
class PlayerTotalsData(models.Model):
    player_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    minutes_played = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_goals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    three_fg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    two_fg = models.DecimalField(max_digits=5, decimal_places=3, null=True)
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
        return self.player_name
    
    
class PlayerAdvancedData(models.Model):
    player_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    minutes_played = models.IntegerField(null=True)
    PER = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    TS_percent = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    three_p_attempt_rate = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    ft_attempt_rate = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    orb_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    drb_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    trb_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ast_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    stl_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    blk_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    tov_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    usg_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ows = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    dws = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ws = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ws_per_48 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    obpm = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    dbpm = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bpm = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    vorp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    
    def __str__(self):
        return self.player_name
    
    
        
        
    

