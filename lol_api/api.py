import requests
from config import BASE_URL, ACCOUNT_URL, HEADERS

# 챌린저 유저 뽑아오기
def fetch_top_players(queue, tier, division, page): 
    solo_league_url = f"{BASE_URL}league-exp/v4/entries/{queue}/{tier}/{division}?page={page}"
    res = requests.get(solo_league_url, headers=HEADERS)

    if 200 <= res.status_code <= 299:
        return res.json()
    else:
        print(f"Error: status code {res.status_code}")
        return None


# Summoner_id로 Puuid 얻기
def get_puuid_by_summoner_id(encrypted_summoner_id):
    puuid_url = f"{BASE_URL}summoner/v4/summoners/{encrypted_summoner_id}"
    res = requests.get(puuid_url, headers=HEADERS)
    return res.json()


# Puuid로 챔피언 마스터리 정보 얻기
def champion_mastery_by_id(puuid):
    url = f"{BASE_URL}champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"
    res = requests.get(url, headers=HEADERS)

    if 200 <= res.status_code <= 299:
        return res.json()
    else:
        print(f"Error: status code {res.status_code}")
        return None

# Puuid로 최근 MatchID 정보 얻기
def get_match_ids_by_puuid(puuid, count):
    url = f"{ACCOUNT_URL}/lol/match/v5/matches/by-puuid/{puuid}/ids?count={count}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

# MatchID로 세부 정보 얻기
def get_match_by_id(match_id):
    url = f"{ACCOUNT_URL}lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

# puuid로 gamename & tagline 열람
def get_summoner_by_puuid(puuid):
    puuid_url = ACCOUNT_URL+ f"/riot/account/v1/accounts/by-puuid/{puuid}"
    res = requests.get(puuid_url, headers=HEADERS)
    json = res.json()
    return json

# Django_user에 저장하기
def save_django_user(puuid, game_name, tag_line, is_pro):
    puuid_url = f"http://127.0.0.1:8000/lol/user/register?puuid={puuid}&game_name={game_name}&tag_line={tag_line}&is_pro={is_pro}"
    res = requests.get(puuid_url, headers=HEADERS)
    json = res.json()
    return json

# Django_match에 저장하기
def save_django_match(top_player, riot_matchID, gamelength, gametype, gameresult):
    match_url = f"http://127.0.0.1:8000/lol/match/register?top_player={top_player}&riot_matchID={riot_matchID}&gamelength={gamelength}&gametype={gametype}&gameresult={gameresult}"
    res = requests.get(match_url, headers=HEADERS)
    json = res.json()
    return json

# Django_match_details에 저장하기
def save_django_match_detail(match, champion_name, kills, deaths, assists, total_damage_dealt, total_minions_killed, gold_earned, gold_spent, time_ccing_others, total_time_cc_dealt, getback_pings, onmyway_pings, needvision_pings, push_pings, total_time_spent_dead):
    match_detail_url = f"http://127.0.0.1:8000/lol/match/detail/register?match={match}&champion_name={champion_name}&kills={kills}&deaths={deaths}&assists={assists}&total_damage_dealt={total_damage_dealt}&total_minions_killed={total_minions_killed}&gold_earned={gold_earned}&gold_spent={gold_spent}&time_ccing_others={time_ccing_others}&total_time_cc_dealt={total_time_cc_dealt}&getback_pings={getback_pings}&onmyway_pings={onmyway_pings}&needvision_pings={needvision_pings}&push_pings={push_pings}&total_time_spent_dead={total_time_spent_dead}"
    res = requests.get(match_detail_url, headers=HEADERS)
    json = res.json()
    return json

