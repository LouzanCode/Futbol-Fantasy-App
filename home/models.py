from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager, PlayerManager




class PlayerPosition(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'positions'
        
    def get_absolute_url(self):
        return reverse('home:position_player', args=[self.slug])

    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'teams'

    def get_absolute_url(self):
        return reverse('home:team', args=[self.slug])

    def __str__(self):
        return self.name



class Player(models.Model):
    
    # Info
    
    name = models.CharField(max_length=50)
    position =  models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, related_name='player')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player')
    nationality = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    altura = models.CharField(max_length=50)
    foot = models.CharField( max_length=50)
    number = models.CharField(max_length=50) 
    market_value = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    points = models.IntegerField(default=0)
    # Stats
    
    matches = models.CharField(max_length=20, blank=True, null=True)  
    started = models.CharField(max_length=20, blank=True, null=True) 
    min_per_game = models.CharField(max_length=20, blank=True, null=True) 
    goals = models.CharField(max_length=20, blank=True, null=True) 
    exp_goals = models.CharField(max_length=20, blank=True, null=True) 
    penalty_goals = models.CharField(max_length=20, blank=True, null=True) 
    penalty_conversion = models.CharField(max_length=20, blank=True, null=True) 
    score_freq = models.CharField(max_length=20, blank=True, null=True) 
    goals_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_shots = models.CharField(max_length=20, blank=True, null=True) 
    shots_per_game = models.CharField(max_length=20, blank=True, null=True) 
    shots_target = models.CharField(max_length=20, blank=True, null=True) 
    shots_on_target_per_game = models.CharField(max_length=20, blank=True, null=True) 
    bigchances_missed = models.CharField(max_length=20, blank=True, null=True) 
    goal_conversion = models.CharField(max_length=20, blank=True, null=True) 
    freekick_goals = models.CharField(max_length=20, blank=True, null=True) 
    freekick_conversion = models.CharField(max_length=20, blank=True, null=True) 
    goals_insidebox = models.CharField(max_length=20, blank=True, null=True) 
    goals_outsidebox = models.CharField(max_length=20, blank=True, null=True) 
    head_goals = models.CharField(max_length=20, blank=True, null=True) 
    left_goals = models.CharField(max_length=20, blank=True, null=True) 
    right_goals = models.CharField(max_length=20, blank=True, null=True) 
    penalty_won = models.CharField(max_length=20, blank=True, null=True) 
    assists = models.CharField(max_length=20, blank=True, null=True) 
    exp_assists = models.CharField(max_length=20, blank=True, null=True) 
    total_touches = models.CharField(max_length=20, blank=True, null=True) 
    touches_per_game = models.CharField(max_length=20, blank=True, null=True) 
    bigchances_created = models.CharField(max_length=20, blank=True, null=True) 
    total_key_passes = models.CharField(max_length=20, blank=True, null=True) 
    key_passes_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_acc_per_game = models.CharField(max_length=20, blank=True, null=True) 
    acc_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_acc_own_half = models.CharField(max_length=20, blank=True, null=True) 
    acc_own_half = models.CharField(max_length=20, blank=True, null=True) 
    total_acc_oppo_half = models.CharField(max_length=20, blank=True, null=True) 
    acc_oppo_half = models.CharField(max_length=20, blank=True, null=True) 
    total_acc_longballs = models.CharField(max_length=20, blank=True, null=True) 
    acc_longballs = models.CharField(max_length=20, blank=True, null=True) 
    total_acc_chipballs = models.CharField(max_length=20, blank=True, null=True) 
    acc_chipballs = models.CharField(max_length=20, blank=True, null=True) 
    total_acc_crosses = models.CharField(max_length=20, blank=True, null=True) 
    acc_crosses = models.CharField(max_length=20, blank=True, null=True) 
    total_interceptions = models.CharField(max_length=20, blank=True, null=True) 
    intercep_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_tackles = models.CharField(max_length=20, blank=True, null=True) 
    tackles_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_poss_won = models.CharField(max_length=20, blank=True, null=True) 
    poss_won = models.CharField(max_length=20, blank=True, null=True) 
    total_dribbled = models.CharField(max_length=20, blank=True, null=True) 
    dribbled_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_clearences = models.CharField(max_length=20, blank=True, null=True) 
    clearences_per_game = models.CharField(max_length=20, blank=True, null=True) 
    errors_leadtoshot = models.CharField(max_length=20, blank=True, null=True) 
    errors_leadtogoal = models.CharField(max_length=20, blank=True, null=True) 
    penalty_commited = models.CharField(max_length=20, blank=True, null=True) 
    total_succ_dribbles = models.CharField(max_length=20, blank=True, null=True) 
    succ_dribbles_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_duels_won = models.CharField(max_length=20, blank=True, null=True) 
    duels_won_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_ground_duels_won = models.CharField(max_length=20, blank=True, null=True) 
    ground_duels_won_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_air_duels_won = models.CharField(max_length=20, blank=True, null=True) 
    air_duels_won_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_poss_lost = models.CharField(max_length=20, blank=True, null=True) 
    poss_lost_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_fouls = models.CharField(max_length=20, blank=True, null=True) 
    fouls_per_game = models.CharField(max_length=20, blank=True, null=True) 
    total_fouled = models.CharField(max_length=20, blank=True, null=True) 
    fouled_per_game = models.CharField(max_length=20, blank=True, null=True) 
    yellows = models.CharField(max_length=20, blank=True, null=True) 
    yellow_reds = models.CharField(max_length=20, blank=True, null=True) 
    reds = models.CharField(max_length=20, blank=True, null=True) 
    
    
    # Config
    
    slug = models.SlugField(max_length=255)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    prlayers = PlayerManager()

    class Meta:
        verbose_name_plural = 'Players'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('home:player_detail', args=[self.slug])
    
    def __str__(self):
        return self.name



    



class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    team = models.ManyToManyField(Player)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    

