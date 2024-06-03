from django.db import models
from main.models import Member

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length= 100);
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveBigIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title