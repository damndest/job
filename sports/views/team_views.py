from django.shortcuts import render, redirect, HttpResponse
from main.models import Member
from sports.models import SportsTeam, SportsPlayer, SportsTeamTalk
from datetime import datetime
from django.http import Http404
from django.core.exceptions import *
from . import init_team_data

# 영문 게임명 -> 한글 게임명 변환하기 위한 딕셔너리
gamename = {
    'baseball' : "야구",
    'football' : "축구",
    'sportsetc' : "기타 스포츠",
}

# 로그인 요청하는 함수
def need_login() -> HttpResponse:
    msg = "<script>"
    msg += "alert('로그인 후 이용하세요.');"
    msg += f"location.href='/main/login';"
    msg += "</script>"
    return HttpResponse(msg)

# 존재하지 않는 팀 페이지에 접근시 처리하는 함수
def invalid_team(game:str) -> HttpResponse:
    msg = "<script>"
    msg += f"alert('팀 정보가 없습니다.');"
    msg += f"location.href='/sports/{game}/team/';"
    msg += "</script>"
    return HttpResponse(msg)

# 존재하지 않는 톡 접근시 처리하는 함수
def invalid_talk(game:str, team_id:int) -> HttpResponse:
    msg = "<script>"
    msg += f"alert('이미 삭제되었거나 존재하지 않는 글입니다. ');"
    msg += f"location.href='/sports/{game}/team/{team_id}';"
    msg += "</script>"
    return HttpResponse(msg)

# 기타 오류 발생 시
def unknown_error(game:str) -> HttpResponse:
    msg = "<script>"
    msg += f"alert('알 수 없는 오류가 발생했습니다.');"
    msg += f"location.href='/sports/{game}/team/';"
    msg += "</script>"
    return HttpResponse(msg)

# --------------------- 실제 뷰 함수 ---------------------

# 팀 리스트 뷰 함수
def teamlist(request, game):
    # DB에 저장된 팀이 없으면 JSON 파일에 저장된 정보를 DB에 저장해서 초기화시켜줌
    if SportsTeam.objects.count() <= 0:
        init_team_data.init_baseball()
        init_team_data.init_football()

    team_list = SportsTeam.objects.filter(team_game=game).values('team_id', 'team_name', 'team_kname', 'team_league', 'team_bgcolor1', 'team_textcolor1', 'team_bgcolor2', 'team_textcolor2')

    for team in team_list:
        team_id = team['team_id']
        team['fan_count'] = SportsTeam.objects.get(team_id=team_id).team_fans.count()
    content = {
        'game' : game,
        'gamename' : gamename[game],
        'team_list' : team_list,
    }
    return render(request, 'sports/team/teamlist.html', content)

# 팀별 세부 페이지 뷰 함수
def team_detail(request, game, team_id):
    try:
        team = SportsTeam.objects.get(team_id=team_id)
        team_talk = SportsTeamTalk.objects.filter(team_talk_team=team_id)
        content = {
            'game' : game,
            'gamename' : gamename[game],
            'team' : team,
            'talk' : team_talk,
        }
        return render(request, 'sports/team/teamdetail.html', content)
    except ObjectDoesNotExist as e:
        return invalid_team(game)
    except Exception as e:
        return unknown_error(game)