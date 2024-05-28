from django.urls import path, re_path
from . import views

# 스포츠 서브앱 URL app_name 설정
app_name = "SPORTS"

urlpatterns = [
    re_path(r'(\d+)/$', views.index, name="I"), # 서브앱 메인(인덱스) 페이지 URL (매개변수는 페이지 번호)
    path('create/', views.create, name="C"), # 새 게시물 생성 URL
    re_path(r'post/(\d+)/$', views.read, name="R"), # 게시물 조회 URL (매개변수는 조회할 게시물의 ID)
    re_path(r'post/(\d+)/update/$', views.update, name="U"), # 게시물 수정 URL (매개변수는 수정할 게시물의 ID)
    re_path(r'post/(\d+)/delete/$', views.delete, name="D"), # 게시물 삭제 URL (매개변수는 삭제할 게시물의 ID)
]
