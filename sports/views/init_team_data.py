from sports.models import SportsTeam
import json

# DB가 비어있을 때 JSON 파일에 저장된 초기 팀 및 선수 정보를 추가해줌

def init_baseball():
    with open("sports/views/baseball_team.json", "r", encoding='UTF-8') as f:
        baseball_team_list = json.load(f)
    
    for team_name in baseball_team_list:
        team = SportsTeam()
        team.team_name = team_name
        team.team_game = 'baseball'
        team.team_league = baseball_team_list[team_name]['team_league']
        team.team_league_k = baseball_team_list[team_name]['team_league_k']
        team.team_kname = baseball_team_list[team_name]['team_kname']
        team.team_ename = baseball_team_list[team_name]['team_ename']
        team.team_intro = baseball_team_list[team_name]['team_intro']
        team.team_hometown = baseball_team_list[team_name]['team_hometown']
        team.team_manager = baseball_team_list[team_name]['team_manager']
        team.team_site = baseball_team_list[team_name]['team_site']
        team.team_bgcolor1 = baseball_team_list[team_name]['team_bgcolor1']
        team.team_bgcolor2 = baseball_team_list[team_name]['team_bgcolor2']
        team.team_textcolor1 = baseball_team_list[team_name]['team_textcolor1']
        team.team_textcolor2 = baseball_team_list[team_name]['team_textcolor2']
        team.save()

def init_football():
    with open("sports/views/football_team.json", "r", encoding='UTF-8') as f:
        football_team_list = json.load(f)
    
    for team_name in football_team_list:
        team = SportsTeam()
        team.team_name = team_name
        team.team_game = 'football'
        team.team_league = football_team_list[team_name]['team_league']
        team.team_league_k = football_team_list[team_name]['team_league_k']
        team.team_kname = football_team_list[team_name]['team_kname']
        team.team_ename = football_team_list[team_name]['team_ename']
        team.team_intro = football_team_list[team_name]['team_intro']
        team.team_hometown = football_team_list[team_name]['team_hometown']
        team.team_manager = football_team_list[team_name]['team_manager']
        team.team_site = football_team_list[team_name]['team_site']
        team.team_bgcolor1 = football_team_list[team_name]['team_bgcolor1']
        team.team_bgcolor2 = football_team_list[team_name]['team_bgcolor2']
        team.team_textcolor1 = football_team_list[team_name]['team_textcolor1']
        team.team_textcolor2 = football_team_list[team_name]['team_textcolor2']
        team.save()