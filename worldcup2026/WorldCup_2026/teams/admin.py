from django.contrib import admin
from .models import Teams, PlayPosition, Players, TechnicalTeamRoles, TechnicalTeam

admin.site.register(TechnicalTeamRoles)

@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ["team_name", "bandera"]
    
@admin.register(Players)
class PlayersAsdmin(admin.ModelAdmin):
    list_display = ["Foto","p_first_name", "p_first_last_name", "p_position", "p_team", "p_is_titular"]
    
@admin.register(PlayPosition)
class PlayPositionAdmin(admin.ModelAdmin):
    list_display = ["Foto","position_name"]

@admin.register(TechnicalTeam)
class ETAdmin(admin.ModelAdmin):
    list_display = ["t_first_name", "t_first_last_name", "t_nationality", "t_team"]