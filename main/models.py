from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
"""
    AbstarctUser 클래스를 상속받으면 기존의 User 모델의 필드와 메서드를
    그대로 사용가능하고 추가적으로 필드만 추가해서 사용가능하다.
    좀 더 자유롭게 커스터마이징 하고 싶으면 AbstractBaseUser 클래스를
    상속 받아서 사용한다.
"""
class Member(AbstractUser):
    member_idx = models.AutoField(primary_key=True);
    user_id = models.CharField(max_length=255, blank=False, null=False, unique=True);
    user_name = models.CharField(max_length=50, blank=False, null=False);
    phone_num = models.CharField(max_length=15, null=False, default=0, unique=True);

    objects = UserManager();

    USERNAME_FIELD = "user_id";
    REQUIRED_FIELDS = ["username", "email"];

    def __str__(self):
        return self.user_id;