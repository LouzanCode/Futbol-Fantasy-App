from django.contrib import admin

from .models import Player, PlayerPosition, Team, CustomUser



# Register your models here.
@admin.register(PlayerPosition)
class PlayerPositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'team', 'position']
    list_filter = ['is_active', ]
    list_editable = ['team', ]
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(CustomUser)