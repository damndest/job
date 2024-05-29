from django.contrib import admin
from .models import BaseballPost, BaseballPostComment

class BaseballPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')

class BaseballPostCommentAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'author')

admin.site.register(BaseballPost, BaseballPostAdmin)
admin.site.register(BaseballPostComment, BaseballPostCommentAdmin)
