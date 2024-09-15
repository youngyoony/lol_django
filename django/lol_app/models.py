from django.db import models

class TopPlayer(models.Model):
    puuid = models.TextField()
    game_name = models.TextField()
    tag_line = models.TextField()
    is_pro = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    

class Match(models.Model):
    top_player = models.ForeignKey(TopPlayer, on_delete=models.CASCADE)
    riot_matchID = models.TextField()
    gamelength = models.TextField()
    gametype = models.TextField()
    gameresult = models.TextField()

    def __str__(self):
        return str(self.id)
    

class MatchDetail(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    champion_id = models.TextField()
    champion_name = models.TextField()
    kills = models.TextField()
    deaths = models.TextField()
    assists = models.TextField()
    total_damage_dealt = models.TextField()
    total_damage_dealt_tochampions = models.TextField()
    total_damage_taken = models.TextField()
    total_minions_killed = models.TextField()
    gold_earned = models.TextField()
    gold_spent = models.TextField()
    time_ccing_others = models.TextField()
    total_time_cc_dealt = models.TextField()
    getback_pings = models.TextField()
    onmyway_pings = models.TextField()
    needvision_pings = models.TextField()
    push_pings = models.TextField()
    total_time_spent_dead = models.TextField()

    def __str__(self):
        return str(self.id)
    