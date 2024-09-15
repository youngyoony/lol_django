from django.contrib import admin
from .models import TopPlayer, Match, MatchDetail

@admin.register(TopPlayer)
class TopPlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'puuid', 'game_name', 'tag_line', 'is_pro')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'top_player', 'riot_matchID', 'gamelength', 'gametype', 'gameresult')
    search_fields = ('riot_matchID', 'top_player__game_name')

@admin.register(MatchDetail)
class MatchDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'match', 'champion_name', 'kills', 'deaths', 'assists', 'total_damage_dealt', 'total_minions_killed', 'gold_earned', 'gold_spent', 'time_ccing_others', 'total_time_cc_dealt', 'getback_pings', 'onmyway_pings', 'needvision_pings', 'push_pings', 'total_time_spent_dead')
    search_fields = ('champion_name', 'match__riot_matchID')