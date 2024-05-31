from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ['member_idx', 'user_id', 'user_name', 'phone_num', 'email'];

admin.site.register(Member, UserAdmin);