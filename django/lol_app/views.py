from django.http import JsonResponse
import requests
from .models import TopPlayer, Match, MatchDetail
from .serializers import TopPlayerSerializer

def save_top_player(request):
    puuid = request.GET.get("puuid")
    game_name = request.GET.get("game_name")
    tag_line = request.GET.get("tag_line")
    is_pro = request.GET.get("is_pro") == "True"

    top_player = TopPlayer(puuid=puuid, game_name=game_name, tag_line=tag_line, is_pro=is_pro)
    top_player.save()
    
    return JsonResponse({
        "code": "success",
    })


def save_match(request):
    top_player_id = request.GET.get("top_player_id")
    riot_matchID = request.GET.get("riot_matchID")
    gamelength = request.GET.get("gamelength")
    gametype = request.GET.get("gametype")
    gameresult = request.GET.get("gameresult")

    try:
        top_player = TopPlayer.objects.get(id=top_player_id)
    except TopPlayer.DoesNotExist:
        return JsonResponse({"code": "error", "message": "TopPlayer not found"})

    match = Match(
        top_player=top_player, 
        riot_matchID=riot_matchID, 
        gamelength=gamelength, 
        gametype=gametype, 
        gameresult=gameresult
    )
    match.save()
    
    return JsonResponse({
        "code": "success",
    })


def save_match_detail(request):
    match_id = request.GET.get("match_id")
    champion_id = request.GET.get("champion_id")
    champion_name = request.GET.get("champion_name")
    kills = request.GET.get("kills")
    deaths = request.GET.get("deaths")
    assists = request.GET.get("assists")
    total_damage_dealt = request.GET.get("total_damage_dealt")
    total_damage_dealt_tochampions = request.GET.get("total_damage_dealt_tochampions")
    total_damage_taken = request.GET.get("total_damage_taken")
    total_minions_killed = request.GET.get("total_minions_killed")
    gold_earned = request.GET.get("gold_earned")
    gold_spent = request.GET.get("gold_spent")
    time_ccing_others = request.GET.get("time_ccing_others")
    total_time_cc_dealt = request.GET.get("total_time_cc_dealt")
    getback_pings = request.GET.get("getback_pings")
    onmyway_pings = request.GET.get("onmyway_pings")
    needvision_pings = request.GET.get("needvision_pings")
    push_pings = request.GET.get("push_pings")
    total_time_spent_dead = request.GET.get("total_time_spent_dead")

    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        return JsonResponse({"code": "error", "message": "Match not found"})

    match_detail = MatchDetail(
        match=match,
        champion_id=champion_id,
        champion_name=champion_name,
        kills=kills,
        deaths=deaths,
        assists=assists,
        total_damage_dealt=total_damage_dealt,
        total_damage_dealt_tochampions=total_damage_dealt_tochampions,
        total_damage_taken=total_damage_taken,
        total_minions_killed=total_minions_killed,
        gold_earned=gold_earned,
        gold_spent=gold_spent,
        time_ccing_others=time_ccing_others,
        total_time_cc_dealt=total_time_cc_dealt,
        getback_pings=getback_pings,
        onmyway_pings=onmyway_pings,
        needvision_pings=needvision_pings,
        push_pings=push_pings,
        total_time_spent_dead=total_time_spent_dead,
    )
    match_detail.save()

    return JsonResponse({
        "code": "success",
    })


def fetch_all_top_players(request):
    top_players = TopPlayer.objects.all()
    top_players_sr = TopPlayerSerializer(top_players, many=True).data

    return JsonResponse({
        "code": "success",
        "data": top_players_sr
    })