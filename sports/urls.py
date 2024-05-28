from django.urls import path, re_path
from . import views

# 스포츠 서브앱 URL app_name 설정
app_name = "sports"

urlpatterns = [
    path('', views.index, name="i"), # 스포츠 서브앱 메인(인덱스) 페이지 URL
    # 스포츠/축구
    re_path(r'football/(\d+)/$', views.f_pagelist, name="f"), # 페이지 목록 URL (매개변수는 페이지 번호)
    path('football/create/', views.f_create, name="f_c"), # 새 게시물 생성 URL
    re_path(r'football/post/(\d+)/$', views.f_read, name="f_r"), # 게시물 조회 URL (매개변수는 게시물 번호)
    re_path(r'football/post/(\d+)/update/$', views.f_update, name="f_u"), # 게시물 수정 URL (매개변수는 게시물 번호)
    re_path(r'football/post/(\d+)/delete/$', views.f_delete, name="f_d"), # 게시물 삭제 URL (매개변수는 게시물 번호)
    # 스포츠/야구
    re_path(r'baseball/(\d+)/$', views.b_pagelist, name="b"), # 페이지 목록 URL (매개변수는 페이지 번호)
    path('baseball/create/', views.b_create, name="b_c"), # 새 게시물 생성 URL
    re_path(r'baseball/post/(\d+)/$', views.b_read, name="b_r"), # 게시물 조회 URL (매개변수는 게시물 번호)
    re_path(r'baseball/post/(\d+)/update/$', views.b_update, name="b_u"), # 게시물 수정 URL (매개변수는 게시물 번호)
    re_path(r'baseball/post/(\d+)/delete/$', views.b_delete, name="b_d"), # 게시물 삭제 URL (매개변수는 게시물 번호)
    # 스포츠/기타
    re_path(r'baseball/(\d+)/$', views.e_pagelist, name="e"), # 페이지 목록 URL (매개변수는 페이지 번호)
    path('baseball/create/', views.e_create, name="e_c"), # 새 게시물 생성 URL
    re_path(r'baseball/post/(\d+)/$', views.e_read, name="e_r"), # 게시물 조회 URL (매개변수는 게시물 번호)
    re_path(r'baseball/post/(\d+)/update/$', views.e_update, name="e_u"), # 게시물 수정 URL (매개변수는 게시물 번호)
    re_path(r'baseball/post/(\d+)/delete/$', views.e_delete, name="e_d"), # 게시물 삭제 URL (매개변수는 게시물 번호)
]
