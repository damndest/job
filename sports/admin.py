from django.contrib import admin
from .models import SportsPost, SportsReply, SportsTeam, SportsPlayer, SportsTeamTalk, SportsPlayerTalk

class SportsPostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'post_title', 'post_author')

class SportsReplyAdmin(admin.ModelAdmin):
    list_display = ('reply_id', 'reply_author')

admin.site.register(SportsPost, SportsPostAdmin)
admin.site.register(SportsReply, SportsReplyAdmin)
