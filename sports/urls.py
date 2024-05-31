from django.urls import path, re_path
from django.views.generic import RedirectView
from .views import base_views, baseball_views, football_views, sportsetc_views

from .views import base_views, board_views, baseball_views, football_views, sportsetc_views

# 스포츠 서브앱 URL app_name 설정
app_name = "sports"

urlpatterns = [
    path('', base_views.index, name="main"), # 스포츠 서브앱 메인(인덱스) 페이지 URL
    path('forbidden/', base_views.forbidden, name="forbidden"),
    # 스포츠/야구
    path('baseball/', baseball_views.baseball, name="baseball"), # 새 게시물 생성 URL
    re_path(r'baseball/board/(\d+)/$', baseball_views.boardlist, name="baseball_board"), # 페이지 목록 URL (매개변수는 페이지 번호)
    path('baseball/board/', RedirectView.as_view(url='/sports/baseball/board/1', permanent=True)), # baseball/board/로 접속 시 baseball_board로 리다이렉트
    path('baseball/board/create/', baseball_views.board_create, name="baseball_board_create"), # 새 게시물 생성 URL
    re_path(r'baseball/board/post/(\d+)/$', baseball_views.board_read, name="baseball_board_read"), # 게시물 조회 URL (매개변수는 게시물 번호)
    path('baseball/board/post/', RedirectView.as_view(url='/sports/baseball/board/1', permanent=True)), # baseball/board/로 접속 시 baseball_board로 리다이렉트
    re_path(r'baseball/board/post/(\d+)/update/$', baseball_views.board_update, name="baseball_board_update"), # 게시물 수정 URL (매개변수는 게시물 번호)
    re_path(r'baseball/board/post/(\d+)/delete/$', baseball_views.board_delete, name="baseball_board_delete"), # 게시물 삭제 URL (매개변수는 게시물 번호)
    re_path(r'baseball/board/post/(\d+)/like/$', baseball_views.board_like, name="baseball_board_like"), # 게시물 좋아요 URL (매개변수는 게시물 번호)
    re_path(r'baseball/board/post/(\d+)/dislike/$', baseball_views.board_dislike, name="baseball_board_dislike"), # 게시물 좋아요 URL (매개변수는 게시물 번호)
    re_path(r'baseball/board/post/(\d+)/addreply', baseball_views.board_add_reply, name="baseball_board_addreply"), # 게시물 댓글 추가 URL (매개변수는 게시물 번호)
    re_path(r'baseball/board/post/delreply/(\d+)', baseball_views.board_del_reply, name="baseball_board_delreply"), # 게시물 댓글 삭제 URL (매개변수는 게시물 번호, 댓글 번호)
    re_path(r'baseball/board/post/replylike/(\d+)', baseball_views.board_reply_like, name="baseball_board_addreply"), # 게시물 댓글 추가 URL (매개변수는 게시물 번호)
    re_path(r'baseball/board/post/replydislike/(\d+)', baseball_views.board_reply_dislike, name="baseball_board_delreply"), # 게시물 댓글 삭제 URL (매개변수는 게시물 번호, 댓글 번호)
    # # 스포츠/축구
    # re_path(r'football/(\d+)/$', views.f_pagelist, name="f"), # 페이지 목록 URL (매개변수는 페이지 번호)
    # path('football/create/', views.f_create, name="f_c"), # 새 게시물 생성 URL
    # re_path(r'football/post/(\d+)/$', views.f_read, name="f_r"), # 게시물 조회 URL (매개변수는 게시물 번호)
    # re_path(r'football/post/(\d+)/update/$', views.f_update, name="f_u"), # 게시물 수정 URL (매개변수는 게시물 번호)
    # re_path(r'football/post/(\d+)/delete/$', views.f_delete, name="f_d"), # 게시물 삭제 URL (매개변수는 게시물 번호)
    # # 스포츠/기타
    # re_path(r'baseball/(\d+)/$', views.e_pagelist, name="e"), # 페이지 목록 URL (매개변수는 페이지 번호)
    # path('baseball/create/', views.e_create, name="e_c"), # 새 게시물 생성 URL
    # re_path(r'baseball/post/(\d+)/$', views.e_read, name="e_r"), # 게시물 조회 URL (매개변수는 게시물 번호)
    # re_path(r'baseball/post/(\d+)/update/$', views.e_update, name="e_u"), # 게시물 수정 URL (매개변수는 게시물 번호)
    # re_path(r'baseball/post/(\d+)/delete/$', views.e_delete, name="e_d"), # 게시물 삭제 URL (매개변수는 게시물 번호)
]
