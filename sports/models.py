from django.db import models

# -------------------------- 공통 추상(abstract) 테이블 정의 --------------------------

# 자유게시판 글 테이블(추상)
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False) # 글 제목
    author = models.CharField(max_length=255, blank=False, null=False) # 글 작성자
    content = models.TextField(null=False) # 글 내용
    wdate = models.DateTimeField(null=False) # 최초 작성일
    udate = models.DateTimeField(null=False) # 최근 수정일
    views = models.IntegerField(null=False) # 조회수
    comment = models.IntegerField(null=False, default=0) # 댓글 수
    class Meta:
        abstract = True

# 자유게시판 댓글 테이블(추상)
class PostComment(models.Model):
    author = models.CharField(max_length=255, null=False) # 댓글 작성자
    content = models.CharField(max_length=255) # 댓글 내용
    wdate = models.DateTimeField(null=False) # 최초 작성일
    class Meta:
        abstract = True

# 팀 테이블(추상)
class Team(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False) # 팀 명
    summary = models.CharField(max_length=255, null=True) # 팀 요약 설명
    hometown = models.CharField(max_length=255, null=True) # 팀 연고지
    stadium = models.CharField(max_length=255, null=True) # 팀 홈 경기장
    manager = models.CharField(max_length=255, null=True) # 팀 감독
    color1 = models.CharField(max_length=8, blank=False, null=False) # 팀 컬러 1
    color2 = models.CharField(max_length=8, blank=False, null=False) # 팀 컬러 2
    class Meta:
        abstract = True

# 선수 테이블(추상)
class Player(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False) # 선수 명
    summary = models.CharField(max_length=255, null=True) # 선수 요약 설명
    stadium = models.DateTimeField(null=True) # 팀 홈 경기장
    class Meta:
        abstract = True

# 톡 테이블(추상)
# 톡 : 특정 팀이나 선수와 관련하여 댓글처럼 짧게 이야기를 나누는 방식
class Talk(models.Model):
    author = models.CharField(max_length=255, null=False) # 톡 작성자
    content = models.CharField(max_length=255) # 톡 내용
    wdate = models.DateTimeField(null=False) # 작성일
    class Meta:
        abstract = True

# 팀 별 톡 테이블(추상)
class TeamTalk(Talk):
    class Meta:
        abstract = True

# 선수 별 톡 테이블(추상)
class PlayerTalk(Talk):
    class Meta:
        abstract = True

# 유저의 팬 관계 테이블(추상)
# 팬 : 유저가 특정 선수나 팀에게 일종의 팔로우 관계를 맺어서 팬으로 등록하는 시스템
# 다대다 테이블처럼 구현
class FanRelation(models.Model):
    user = models.CharField(max_length=255, null=False) # 관계 맺는 유저명
    class Meta:
        abstract = True

# 팀 - 유저 팬 관계 테이블
class TeamFanRelation(models.Model):
    class Meta:
        abstract = True

# 선수 - 유저 팬 관계 테이블
class PlayerFanRelation(models.Model):
    class Meta:
        abstract = True

# -------------------------- 실제(Concrete) 테이블 정의 --------------------------


# 야구 게시판 글 테이블
class BaseballPost(Post):
    pass

# 야구 게시판 댓글 테이블
class BaseballPostComment(PostComment):
    post_id = models.ForeignKey("BaseballPost", related_name="post", on_delete=models.CASCADE, db_column="post_id") # 댓글이 작성된 게시글의 ID(외래키)

# 축구 게시판 글 테이블
class FootballPost(Post):
    pass

# 축구 게시판 댓글 테이블
class FootballPostComment(PostComment):
    post_id = models.ForeignKey("FootballPost", related_name="post", on_delete=models.CASCADE, db_column="post_id") # 댓글이 작성된 게시글의 ID(외래키)

# 기타 스포츠 게시판 글 테이블
class SportsEtcPost(Post):
    pass

# 기타 스포츠 게시판 댓글 테이블
class SportsEtcPostComment(PostComment):
    post_id = models.ForeignKey("SportsEtcPost", related_name="post", on_delete=models.CASCADE, db_column="post_id", blank=False, null=False) # 댓글이 작성된 게시글의 ID(외래키)

# 야구 팀 테이블
class BaseballTeam(Team):
    pass

# 축구 팀 테이블
class FootballTeam(Team):
    pass

# 기타 스포츠 팀 테이블
class SportsEtcTeam(Team):
    pass

# 야구 선수 테이블
class BaseballPlayer(Player):
    team = models.ForeignKey("BaseballTeam", related_name="own_team", on_delete=models.SET_NULL, null=True) # 선수가 소속된 팀 ID(외래키)

# 축구 선수 테이블
class FootballPlayer(Player):
    team = models.ForeignKey("FootballTeam", related_name="own_team", on_delete=models.SET_NULL, null=True) # 선수가 소속된 팀 ID(외래키)

# 기타 스포츠 선수 테이블
class SportsEtcPlayer(Player):
    team = models.ForeignKey("SportsEtcTeam", related_name="own_team", on_delete=models.SET_NULL, null=True) # 선수가 소속된 팀 ID(외래키)

# 야구 팀 톡 테이블
class BaseballTeamTalk(Talk):
    team = models.ForeignKey("BaseballTeam", related_name="subject_team", on_delete=models.CASCADE, null=False) # 대상 야구 팀 ID(외래 키)

# 축구 팀 톡 테이블
class FootballTeamTalk(Talk):
    team = models.ForeignKey("FootballTeam", related_name="subject_team", on_delete=models.CASCADE, null=False) # 대상 축구 팀 ID(외래 키)

# 기타 스포츠 팀 톡 테이블
class SportsEtcTeamTalk(Talk):
    team = models.ForeignKey("SportsEtcTeam", related_name="subject_team", on_delete=models.CASCADE, null=False) # 대상 기타 스포츠 팀 ID(외래 키)

# 야구 선수 톡 테이블
class BaseballPlayerTalk(Talk):
    player = models.ForeignKey("BaseballPlayer", related_name="subject_player", on_delete=models.CASCADE, null=False) # 대상 야구 선수 ID(외래 키)

# 축구 선수 톡 테이블
class FootballPlayerTalk(Talk):
    player = models.ForeignKey("FootballPlayer", related_name="subject_player", on_delete=models.CASCADE, null=False) # 대상 축구 선수 ID(외래 키)

# 기타 스포츠 선수 톡 테이블
class SportsEtcPlayerTalk(Talk):
    player = models.ForeignKey("SportsEtcPlayer", related_name="subject_player", on_delete=models.CASCADE, null=False) # 대상 스포츠 선수 ID(외래 키)

# 야구 팀 팬 관계 테이블
class BaseballTeamFanRelation(TeamFanRelation):
    team = models.ForeignKey("BaseballTeam", related_name="following_team", on_delete=models.CASCADE, null=False) # 관계 맺는 야구 팀 ID(외래 키)

# 축구 팀 팬 관계 테이블
class FootballTeamFanRelation(TeamFanRelation):
    team = models.ForeignKey("FootballTeam", related_name="following_team", on_delete=models.CASCADE, null=False) # 관계 맺는 축구 팀 ID(외래 키)

# 기타 스포츠 팀 관계 테이블
class SportsEtcTeamFanRelation(TeamFanRelation):
    team = models.ForeignKey("SportsEtcTeam", related_name="following_team", on_delete=models.CASCADE, null=False) # 관계 맺는 기타 스포츠 팀 ID(외래 키)

# 야구 선수 팬 관계 테이블
class BaseballPlayerFanRelation(PlayerFanRelation):
    player = models.ForeignKey("BaseballPlayer", related_name="following_player", on_delete=models.CASCADE, null=False) # 관계 맺는 야구 선수 ID(외래 키)

# 축구 선수 팬 관계 테이블
class FootballPlayerFanRelation(PlayerFanRelation):
    player = models.ForeignKey("FootballPlayer", related_name="following_player", on_delete=models.CASCADE, null=False) # 관계 맺는 축구 선수 ID(외래 키)

# 기타 스포츠 선수 팬 관계 테이블
class SportsEtcPlayerFanRelation(PlayerFanRelation):
    player = models.ForeignKey("SportsEtcPlayer", related_name="f0llowing_player", on_delete=models.CASCADE, null=False) # 관계 맺는 기타 스포츠 선수 ID(외래 키)