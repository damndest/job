from django.db import models
from main.models import Member

# -------------------------- 공통 추상(abstract) 테이블 정의 --------------------------

# 자유게시판 글 테이블
class SportsPost(models.Model):
    post_id = models.AutoField(primary_key=True) # 게시글 ID(PK)
    post_game = models.CharField(max_length=64, null=False) # 종목 구분(야구, 축구, 기타)
    post_author = models.CharField(max_length=255, null=False) # 작성한 유저 아이디(조인 없이 직접 저장)
    post_author_nn = models.CharField(max_length=255, null=False) # 작성한 유저 닉네임(옵션)
    post_title = models.CharField(max_length=255, null=False, blank=False) # 게시글 제목
    post_content = models.TextField(null=False) # 게시글 내용
    post_wdate = models.DateTimeField(null=False) # 최초 작성일
    post_udate = models.DateTimeField(null=False) # 최근 수정일
    post_views = models.IntegerField(null=False) # 조회수
    post_member = models.ForeignKey(Member, on_delete=models.CASCADE) # 작성한 유저 인덱스(FK)
    post_like = models.ManyToManyField(Member, related_name='liked_post') # 좋아요 누른 사람(Member 객체와 다대다 관계)
    post_dislike = models.ManyToManyField(Member, related_name='disliked_post') # 싫어요 누른 사람(Member 객체와 다대다 관계)

# 자유게시판 댓글 테이블
class SportsReply(models.Model):
    reply_id = models.AutoField(primary_key=True) # 댓글 ID(PK)
    reply_author = models.CharField(max_length=255, null=False) # 댓글 작성자 아이디
    reply_author_nn = models.CharField(max_length=255, null=True, default=reply_author) # 댓글 작성자 닉네임(옵션)
    reply_content = models.CharField(max_length=255, null=False, blank=False) # 댓글 내용
    reply_wdate = models.DateTimeField(null=False) # 최초 작성일
    reply_member = models.ForeignKey(Member, on_delete=models.CASCADE) # 댓글 작성자 인덱스(FK)
    post_id = models.ForeignKey(SportsPost, on_delete=models.CASCADE, related_name='post_reply') # 댓글의 원 글 아이디(FK)
    reply_like = models.ManyToManyField(Member, related_name='liked_reply') # 좋아요 누른 사람(Member 객체와 다대다 관계)
    reply_dislike = models.ManyToManyField(Member, related_name='disliked_reply') # 싫어요 누른 사람(Member 객체와 다대다 관계)

# 스포츠 팀 테이블
class SportsTeam(models.Model):
    team_id = models.AutoField(primary_key=True) # 팀 ID(PK)
    team_name = models.CharField(max_length=255, blank=False, null=False) # 팀 명
    team_game = models.CharField(max_length=64, null=False) # 팀 종목(야구, 축구, 기타)
    team_league = models.CharField(max_length=128, null=True) # 팀 소속 리그
    team_intro = models.CharField(max_length=255, null=True) # 팀 요약 설명
    team_hometown = models.CharField(max_length=255, null=True) # 팀 연고지
    team_manager = models.CharField(max_length=255, null=True) # 팀 감독
    team_site = models.CharField(max_length=512, null=True) # 팀 공식 사이트 주소
    team_color1 = models.CharField(max_length=16, null=True) # 팀 컬러 1
    team_color2 = models.CharField(max_length=16, null=True) # 팀 컬러 2
    team_color3 = models.CharField(max_length=16, null=True) # 팀 컬러 1
    team_color4 = models.CharField(max_length=16, null=True) # 팀 컬러 2
    team_fans = models.ManyToManyField(Member, related_name='liked_team') # 팀과 팬 관계(팔로우) 맺은 사람(Member 객체와 다대다 관계)

# 스포츠 선수 테이블
class SportsPlayer(models.Model):
    player_id = models.AutoField(primary_key=True) # 선수 ID(PK)
    player_name = models.CharField(max_length=255, blank=False, null=False) # 선수 명
    player_game = models.CharField(max_length=64, null=False) # 선수 종목(야구, 축구, 기타)
    player_birthdate = models.DateField(null=True) # 생년월일
    player_intro = models.CharField(max_length=255, null=True) # 선수 요약 설명
    player_uniform_number = models.IntegerField(null=True) # 등번호
    player_team = models.ForeignKey(SportsTeam, on_delete=models.SET_NULL, null=True) # 소속팀 인덱스
    player_fans = models.ManyToManyField(Member, related_name='liked_player') # 팀과 팬 관계(팔로우) 맺은 사람(Member 객체와 다대다 관계)

# ===================== 이 아래는 공사 중 =====================

# 스포츠 팀 톡 테이블
class SportsTeamTalk(models.Model):
    team_talk_id = models.AutoField(primary_key=True) # 톡 ID (PK)
    team_talk_author = models.CharField(max_length=255, null=False) # 톡 작성자
    team_talk_content = models.CharField(max_length=255) # 톡 내용
    team_talk_wdate = models.DateTimeField(null=False) # 작성일
    team_talk_team = models.ForeignKey(SportsTeam, on_delete=models.CASCADE)
    team_talk_member = models.ForeignKey(Member, on_delete=models.CASCADE)

# 스포츠 선수 톡 테이블
class SportsPlayerTalk(models.Model):
    player_talk_id = models.AutoField(primary_key=True) # 톡 ID (PK)
    player_talk_author = models.CharField(max_length=255, null=False) # 톡 작성자
    player_content = models.CharField(max_length=255) # 톡 내용
    player_wdate = models.DateTimeField(null=False) # 작성일
    player_talk_player = models.ForeignKey(SportsPlayer, on_delete=models.CASCADE)
    player_talk_member = models.ForeignKey(Member, on_delete=models.CASCADE)


