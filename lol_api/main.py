import pandas as pd
import time
import json
from api import (
    fetch_top_players, 
    get_puuid_by_summoner_id, 
    champion_mastery_by_id, 
    get_match_ids_by_puuid, 
    get_match_by_id,
    get_summoner_by_puuid,
    save_django_user,
    save_django_match,
    save_django_match_detail
)
from utils import save_csv, read_csv

queue = "RANKED_SOLO_5x5"
tier = "CHALLENGER"
division = "I"
bottom_pro_puuid_list = ['5RK3XGAPbFAg5pV1F89bYLq3TsMx-oxdnvjSAvgb2of5V_9ioZE8jLnAtN8w0CtTMK-4kAGriaomvg', 'hQxVpkcrGq3B7ZXTK5goHDFoSIV6sKq2YMclhKY3xuUI4SLiT-tnnmO7511AeXQTxsfovbFCPDaXdA', 'NVNi020y0qc0LaxD-5TiJJ6IgjSjw5f64w3o-yJjH1CQYHh1XB_79v_vl7iuXAOLEZgLGRRADLfm1Q', 'y7UrJze6eQ0Ob7-iI6-3BY8u2hKJtZkw757Mv2qQVv-keV7VX7UhXt8My_tNJCqcUFzutCELuIQtsQ', 'EihUBkuAtJijWthTeBnmDPmpLwl6Lnm5A9gOE0R6hCQIWkf5NU7dMpAx8NkIRGWb-2yUVzhU36ipJg', 'nVbKQLcIxz8ycuik8wnCbZbhHCkCu0DcrL225mVm4QDCNQ_EWLfWFy8lKt2angLOrEUJpFJy3lg3LA', 'Vaa7P92CXrATNexgYEEejqndZw4ddLtu2sYuhFBDenbevzfD1FkBIU9TgmYLwR9oxyjD-YXvDMavOg', 'yhltIXbJR-9EHDGHAeGn5i0Xh_gCvpDp2MAariLjUofpvHnnh3QDz6Hd8tSxzp1B2AY0R43W3eyofA', 'BIrLC7Jbd1kjqVuwvitoZ70f_qQDf03BqwP7AL2UAvD1t3iDxv9wDNLJnonBwiizIrDNB4E1kN1vhg', 'EFpdViPJWBpenpjdgy2lM6cd-f1WUNPOrgf5r8dB3_DgZSIec-GpK5umeVPF8CJtVAPZUR5YPGco-w', '-J_oN1AB9j-zobSFG5_DWCYkd6mi4EHxd4XvdPUrE9NUbHgCUFaP64vGJxsjV0AmLdm2-ZlkV7Ufcw','VECjfu0_2pPA5Pyx_Qaj7UMheKHVbK5BC5jSYyYO7879FCaqRnhnhG93_cfu1f9eQnaJTYUTdzWqKg', '9WaB3DJ-OPETflKez_IabmAq_oyIKNRsygzecEJhR0zBRNp-jLsDf5YNPuKcR1zuRS0o4Q7AO1Ke-Q', '0calFwO82ODk3acx0pWDxAP-5uOxx2XxaQG_0VPDeRzlo-J961Pf53goollzcxGmGHle-X6bXCuBuQ', '3dslPLp92S6zy3QpgYvzHmq5mQQaazR4mVGn_rTWyqxGoJThDytrrzF2tWSDpz5feyz7pxL8Co8cRw','6M9NUsDLJVpe3q6kIdZ8sd8xpJFNYzcuioe7eVxOQhcHrwdo6EzoPbGl1LDueLsqIRIusn-Za8bkCw','stt4JcSsSLdhpekQ5pS3fhZRHTZFZFBrqEDY5hWfG0tP-Qorgb6rvnFbUXjWK3K6bp0oOPkqvyUoUg','Yj5Lg-6KNsfyhCykWLCboRlIoy5kdiXaJRuAIuR8919T4HAR3HYpl7nOL7lCbbXQJCMULyRVUuRUDw','3sRfpRJ-7sBYbX5vhnzsBEBj2Fk-xg4k4qgEP6MnXJMyOmcEd3p_wp2YI6Qo5T43atnE4ZwlAYWloA','70IGi4Ao7se8RNteuPIdZVDHd_oa2lFXdmZsx8iop-FtrKgHEB2_XmpKMJtDNC41onwVpAXfoOc_PQ','ZvTfThdBAMfKVa6XIAjEZOfb2Aakt_xMsZyHAePRS7XIHjQx1_HbTPA94Y4qt4aUZ1gJ32BscU4UAw','dQ4hU8TFVvvuF2cnYikI-FBAcTkassIXvCvsPkRNeU6sMn4Kws5-5UneTHePIvTaWcCvd7MWm3cTjA']



# 탑 선수들 리스트업

def fetch_all_puuids(top_players, start_idx, end_idx):
    top_player_puuid_list = []
    for i, top_player in enumerate(top_players):
        if start_idx <= i < end_idx:
            print(i)
            top_player_puuid = get_puuid_by_summoner_id(top_player['summonerId'])['puuid']
            top_player_puuid_list.append(top_player_puuid)
    return top_player_puuid_list


# 탑 선수들 리스트업 (CSV 저장)

def get_all_top_player_puuids():
    top_players = fetch_top_players(queue, tier, division, 1)
    top_player_puuid_list = fetch_all_puuids(top_players, 0, 50)
    
    time.sleep(120)
    top_player_puuid_list += fetch_all_puuids(top_players, 50, 100)
    
    time.sleep(120)
    top_player_puuid_list += fetch_all_puuids(top_players, 100, 150)
    
    time.sleep(120)
    top_player_puuid_list += fetch_all_puuids(top_players, 150, 205)
    
    top_players_2nd = fetch_top_players(queue, tier, division, 2)
    
    time.sleep(120)
    top_player_puuid_list += fetch_all_puuids(top_players_2nd, 0, 50)
    
    time.sleep(120)
    top_player_puuid_list += fetch_all_puuids(top_players_2nd, 50, 100)
    
    return top_player_puuid_list


# (저장된 CSV에서) Bottom 선수들 필터링
def filter_bottom_players(top_player_puuid_list, bottom_champ_list):
    bottom_puuid_list = []
    batch_size = 30
    total_puuids = len(top_player_puuid_list)

    for start_idx in range(0, total_puuids, batch_size):
        end_idx = min(start_idx + batch_size, total_puuids)
        batch = top_player_puuid_list[start_idx:end_idx]
        
        for puuid in batch:
            mastery_list = champion_mastery_by_id(puuid)

            if mastery_list is None:
                break

            bottom_cnt = 0

            for mastery in mastery_list:
                if mastery['championId'] in bottom_champ_list:
                    bottom_cnt += 1
            if bottom_cnt > 1:
                bottom_puuid_list.append(puuid)
        
        # 30개의 PUUID를 처리한 후 120초 대기
        if end_idx < total_puuids:
            time.sleep(120)
    
    return bottom_puuid_list


# Bottom 선수들의 최근 매치ID 추출
def fetch_matches_for_players(bottom_puuid_list, num_matches):
    bottom_top_player_match_list = []
    for puuid in bottom_puuid_list:
        match_ids = get_match_ids_by_puuid(puuid, num_matches)

        if isinstance(match_ids, dict) and 'status' in match_ids:
            print(f"Error for PUUID {puuid}: {match_ids['status']['message']}")
            continue

        match_dict = {
            'puuid': puuid,
            'match_ids': match_ids
        }
        bottom_top_player_match_list.append(match_dict)
    return bottom_top_player_match_list

## 이 아래가 주피터
    top_player_match_list = []
    for puuid in top_player_puuid_list: #1명 골랐고
        match_ids = get_match_ids_by_puuid(puuid, 5) #1사람의 5개 매치 리스트를 가져온 것
        match_dict = {
            'puuid': puuid,
            'match_ids': match_ids
        }
        top_player_match_list.append(match_dict)


# Bottom 선수들의 최근 매치ID의 매치 디테일 추출
def fetch_match_data(bottom_top_player_match_list):
    bottom_top_player_match_data_list = []
    batch_size = 50  # 한번에 처리할 매치 디테일
    total_matches = len(bottom_top_player_match_list)
    
    for start_idx in range(0, total_matches, batch_size):
        end_idx = min(start_idx + batch_size, total_matches)
        batch = bottom_top_player_match_list[start_idx:end_idx]
        
        for bottom_top_player_match in batch:
            match_data_list = []
            
            for match_id in bottom_top_player_match['match_ids']:
                match = get_match_by_id(match_id)
                participants = match['info']['participants']

                match_data = None
                for item in participants:
                    if item['puuid'] == bottom_top_player_match['puuid']:
                        match_data = item
                        break

                match_data_list.append(match_data)

            bottom_top_player_match_data_list.append({
                'puuid': bottom_top_player_match['puuid'],
                'match_data_list': match_data_list
            })
        
        # 50개의 매치 데이터를 처리한 후 120초 대기
        if end_idx < total_matches:
            time.sleep(120)
    
    return bottom_top_player_match_data_list


def main():

    '''
    top_player_puuid_list = get_all_top_player_puuids() # 챌린저 플레이어 CSV 저장
    save_csv(top_player_puuid_list, 'top_player_puuid_list', ['puuid'])
    print("top_player_puuid_list.csv saved.")

    top_player_pdlist_pre = read_csv('top_player_puuid_list') # 챌린저 플레이어 불러오기
    top_player_pdlist = top_player_pdlist_pre['puuid'].tolist()
    print("top_player_puuid_list.csv loaded.")

    bottom_champ_list = [523, 22, 51, 119, 81, 202, 222, 145, 429, 96, 236, 21, 895, 360, 235, 15, 18, 29, 110, 67, 498, 221]
    bottom_puuid_list = filter_bottom_players(top_player_pdlist, bottom_champ_list) # Bot 플레이어 필터링 CSV 저장
    save_csv(bottom_puuid_list, 'bottom_puuid_list', ['puuid'])
    print("bottom_puuid_list.csv saved.")
    '''

    bottom_puuid_pdlist_pre = read_csv('bottom_puuid_list', ['puuid']) # Bot 플레이어 필터링 CSV 불러오기
    bottom_puuid_list = bottom_puuid_pdlist_pre['puuid'].tolist()
    print("bottom_puuid_list.csv loaded.")
    
    for item in bottom_puuid_list:
        summoner = get_summoner_by_puuid(item) # 딕셔너리
        
        if summoner['puuid'] in bottom_pro_puuid_list:
            summoner['is_pro'] = True
        else:
            summoner['is_pro'] = False
        
        puuid = summoner['puuid']
        game_name = summoner['gameName']
        tag_line = summoner['tagLine']
        is_pro = summoner['is_pro']
        response = save_django_user(puuid, game_name, tag_line, is_pro)
        print(f"Saved {game_name} with response: {response}")

    # for item in bottom_puuid_list:
    #     summoner = get_summoner_by_puuid(item) # 딕셔너리
    #     response = save_django(
    #                 summoner['puuid'], 
    #                 summoner['gameName'], 
    #                 summoner['tagLine'], 
    #                 summoner['puuid'] in bottom_pro_puuid_list)
    #     print(f"Saved {game_name} with response: {response}")

    bottom_top_player_match_list = fetch_matches_for_players(bottom_puuid_list, 10) # 최근 10경기 불러와서 CSV 저장
    for entry in bottom_top_player_match_list:
        entry['match_ids'] = json.dumps(entry['match_ids'])
    save_csv(bottom_top_player_match_list, 'bottom_top_player_match_list', ['puuid', 'match_ids'])
    print("bottom_top_player_match_list.csv saved.")

    '''
    bottom_top_player_match_list_pre = read_csv('bottom_top_player_match_list', ['puuid', 'match_ids']) # 최근 10경기 CSV 불러오기
    bottom_top_player_match_list_pre['match_ids'] = bottom_top_player_match_list_pre['match_ids'].apply(json.loads)
    bottom_top_player_match_list = bottom_top_player_match_list_pre.to_dict(orient='records')
    print("bottom_top_player_match_list.csv loaded.")

    bottom_top_player_match_data_list = fetch_match_data(bottom_top_player_match_list[0:5]) # 최근 10경기 매치 데이터
    save_csv(bottom_top_player_match_data_list, 'bottom_top_player_match_data_list', ['puuid', 'match_data_list'])
    print("bottom_top_player_match_data_list.csv saved.")
    '''

if __name__ == "__main__":
    main()