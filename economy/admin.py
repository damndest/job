from django.contrib import admin
from economy.models import Border  # ***2번 admin 슈퍼게정 생성 및 어드민.파이 작성해야 admin페이지에서 나옴
# from .models import Border
class borderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'writer', 'writetime', 'updatetime', 'hits')

admin.site.register(Border, borderAdmin)
# Register your models here.


# from 앱폴더.models import 모델
# class 모델이름Admin(admin.ModelAdmin):
#     list_display = ('컬럼명1', '컬럼명2')
# admin.site.register(모델이름, 모델이름Admin)
