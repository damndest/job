from django.db import models
from main.models import Member

# Create your models here.
class Food(models.Model):
    food_no = models.AutoField(primary_key=True);
    writer = models.CharField(max_length=50, blank=False, null=False);
    title = models.CharField(max_length=255, blank=False, null=False);
    content = models.TextField(null=False);
    food_type = models.CharField(max_length=100);
    area_name = models.CharField(max_length=255);
    regist_date = models.DateTimeField(null=False);
    modify_date = models.DateTimeField(null=False);
    see_cnt = models.IntegerField(default=0);
    member_idx = models.ForeignKey(
        Member, on_delete=models.CASCADE
    );

    def __str__(self):
        return self.title;