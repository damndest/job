from django.db import models

# 야구 게시판 글 테이블
class BaseballPost(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False) # 글 제목
    author = models.CharField(max_length=255, blank=False, null=False) # 글 작성자
    content = models.TextField(null=False) # 글 내용
    wdate = models.DateTimeField(null=False) # 최초 작성일
    udate = models.DateTimeField(null=False) # 최근 수정일
    views = models.IntegerField(null=False) # 조회수
    comment = models.IntegerField(null=False, default=0) # 댓글 수

# 야구 게시판 댓글 테이블
class BaseballPostComment(models.Model):
    post_id = models.ForeignKey("BaseballPost", related_name="post", on_delete=models.CASCADE, db_column="post_id") # 댓글이 작성된 게시글의 ID(외래키)
    author = models.CharField(max_length=255, null=False) # 댓글 작성자
    content = models.CharField(max_length=255) # 댓글 내용
    wdate = models.DateTimeField(null=False) # 최초 작성일




