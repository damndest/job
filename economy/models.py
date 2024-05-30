from django.db import models



class Border(models.Model):
    # 컬럼명 = 데이터자료형
    title = models.CharField(max_length=255, blank=False, null=False)
    writer = models.CharField(max_length=255, blank=False, null=False)
    contents = models.TextField(null=False)
    writetime = models.DateTimeField(null=False)
    updatetime = models.DateTimeField(null=False)
    hits = models.IntegerField(null=False)
    # default : 객체 생성할 때 기본값
    # 댓글수 = models.IntegerField(null=False, default=0)
    # 좋아요 = models.IntegerField(null=False, default=0)
    # 싫어요 = models.IntegerField(null=False, default=0)

# Create your models here.
