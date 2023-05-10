from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    minutes_played = models.IntegerField(null=True)
    field_goals = models.IntegerField(null=True)
    field_attempts = models.IntegerField(null=True)
    field_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    three_fg = models.IntegerField(null=True)
    three_attempts = models.IntegerField(null=True)
    three_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    two_fg = models.IntegerField(null=True)
    two_attempts = models.IntegerField(null=True)
    two_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    effect_fg_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    ft = models.IntegerField(null=True)
    fta = models.IntegerField(null=True)
    ft_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    ORB= models.IntegerField(null=True)
    DRB = models.IntegerField(null=True)
    TRB = models.IntegerField(null=True)
    AST = models.IntegerField(null=True)
    STL = models.IntegerField(null=True)
    BLK = models.IntegerField(null=True)
    TOV = models.IntegerField(null=True)
    PF = models.IntegerField(null=True)
    PTS = models.IntegerField(null=True)
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)
    
    def __str__(self):
        return self.player_name
    
    
class PlayerAdvancedData(models.Model):
    player_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    minutes_played = models.IntegerField(null=True)
    PER = models.DecimalField(max_digits=6, decimal_places=1, null=True)
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
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)
    
    def __str__(self):
        return self.player_name
    

class PlayerPlayoffTotalsData(models.Model):
    player_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    minutes_played = models.IntegerField(null=True)
    field_goals = models.IntegerField(null=True)
    field_attempts = models.IntegerField(null=True)
    field_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    three_fg = models.IntegerField(null=True)
    three_attempts = models.IntegerField(null=True)
    three_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    two_fg = models.IntegerField(null=True)
    two_attempts = models.IntegerField(null=True)
    two_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    effect_fg_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    ft = models.IntegerField(null=True)
    fta = models.IntegerField(null=True)
    ft_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    ORB= models.IntegerField(null=True)
    DRB = models.IntegerField(null=True)
    TRB = models.IntegerField(null=True)
    AST = models.IntegerField(null=True)
    STL = models.IntegerField(null=True)
    BLK = models.IntegerField(null=True)
    TOV = models.IntegerField(null=True)
    PF = models.IntegerField(null=True)
    PTS = models.IntegerField(null=True)
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)
    
    def __str__(self):
        return self.player_name


class PlayerPlayoffAdvancedData(models.Model):
    player_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    minutes_played = models.IntegerField(null=True)
    PER = models.DecimalField(max_digits=6, decimal_places=1, null=True)
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
    obpm = models.DecimalField(max_digits=5, decimal_places=2, null=True, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    dbpm = models.DecimalField(max_digits=5, decimal_places=2, null=True, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    bpm = models.DecimalField(max_digits=5, decimal_places=2, null=True, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    vorp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)
    
    def cap_extreme_values(self):
        min_value = -100
        max_value = 100
        
        obpm = float(self.obpm)
        if obpm < min_value:
            obpm = min_value
        elif obpm > max_value:
            obpm = max_value
        self.obpm = obpm

        dbpm = float(self.dbpm)
        if dbpm < min_value:
            dbpm = min_value
        elif dbpm > max_value:
            dbpm = max_value
        self.dbpm = dbpm

        bpm = float(self.bpm)
        if bpm < min_value:
            bpm = min_value
        elif bpm > max_value:
            bpm = max_value
        self.bpm = bpm


    def save(self, *args, **kwargs):
        self.cap_extreme_values()
        super(PlayerPlayoffAdvancedData, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.player_name
    

class PlayerSalaryData(models.Model):
    player_name = models.CharField(max_length=255, null=True)
    salary = models.IntegerField(null=True)
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)
    
    def __str__(self):
        return self.player_name


class PlayerShotChartData(models.Model):
    player_name = models.CharField(max_length=255,  default='')
    top = models.IntegerField(null=True)
    left = models.IntegerField(null=True)
    date = models.CharField(max_length=255,  default='')
    qtr = models.CharField(max_length=6,  default='')
    time_remaining = models.IntegerField(null=True)
    result = models.BooleanField(null=True)
    shot_type = models.CharField(max_length=6,  default='')
    distance_ft = models.IntegerField(null=True)
    lead = models.BooleanField(null=True)
    lebron_team_score = models.IntegerField(null=True)
    opponent_team_score = models.IntegerField(null=True)
    opponent = models.CharField(max_length=30, default='')
    team = models.CharField(max_length=30, default='')
    season = models.IntegerField(null=True)

    def __str__(self):
        return self.player_name
    

    
    
    
        
        
    

