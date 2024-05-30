from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import Member

# Register your models here.
class MemberAdmin(UserAdmin):
    model = Member();

    list_display = ['member_idx', 'user_id', 'email', 'phone_num'];

admin.site.register(Member, MemberAdmin);