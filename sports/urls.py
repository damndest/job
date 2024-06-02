from django.urls import path, re_path
from django.views.generic import RedirectView
from .views import base_views, baseball_views, football_views, sportsetc_views

from .views import base_views, board_views, baseball_views, football_views, sportsetc_views

# 스포츠 서브앱 URL app_name 설정
app_name = "sports"

urlpatterns = [
    path('', base_views.index, name="main"), # 스포츠 서브앱 메인(인덱스) 페이지 URL
    path('forbidden/', base_views.forbidden, name="forbidden"), # Forbidden 페이지 URL

    # 스포츠/야구
    path('baseball/', baseball_views.baseball, name="baseball"), # 야구 페이지 메인 URL
    # path('baseball/', baseball_views.baseball, name="baseball"), # 야구 페이지 메인 URL
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


    # 스포츠/축구
    path('football/', football_views.football, name="football"), # 축구 페이지 메인 URL
    re_path(r'football/board/(\d+)/$', football_views.boardlist, name="football_board"), # 페이지 목록 URL (매개변수는 페이지 번호)
    path('football/board/', RedirectView.as_view(url='/sports/football/board/1', permanent=True)), # football/board/로 접속 시 football_board로 리다이렉트
    path('football/board/create/', football_views.board_create, name="football_board_create"), # 새 게시물 생성 URL
    re_path(r'football/board/post/(\d+)/$', football_views.board_read, name="football_board_read"), # 게시물 조회 URL (매개변수는 게시물 번호)
    path('football/board/post/', RedirectView.as_view(url='/sports/football/board/1', permanent=True)), # football/board/로 접속 시 football_board로 리다이렉트
    re_path(r'football/board/post/(\d+)/update/$', football_views.board_update, name="football_board_update"), # 게시물 수정 URL (매개변수는 게시물 번호)
    re_path(r'football/board/post/(\d+)/delete/$', football_views.board_delete, name="football_board_delete"), # 게시물 삭제 URL (매개변수는 게시물 번호)
    re_path(r'football/board/post/(\d+)/like/$', football_views.board_like, name="football_board_like"), # 게시물 좋아요 URL (매개변수는 게시물 번호)
    re_path(r'football/board/post/(\d+)/dislike/$', football_views.board_dislike, name="football_board_dislike"), # 게시물 좋아요 URL (매개변수는 게시물 번호)
    re_path(r'football/board/post/(\d+)/addreply', football_views.board_add_reply, name="football_board_addreply"), # 게시물 댓글 추가 URL (매개변수는 게시물 번호)
    re_path(r'football/board/post/delreply/(\d+)', football_views.board_del_reply, name="football_board_delreply"), # 게시물 댓글 삭제 URL (매개변수는 게시물 번호, 댓글 번호)
    re_path(r'football/board/post/replylike/(\d+)', football_views.board_reply_like, name="football_board_addreply"), # 게시물 댓글 추가 URL (매개변수는 게시물 번호)
    re_path(r'football/board/post/replydislike/(\d+)', football_views.board_reply_dislike, name="football_board_delreply"), # 게시물 댓글 삭제 URL (매개변수는 게시물 번호, 댓글 번호)


    # 스포츠/기타
    path('sportsetc/', sportsetc_views.sportsetc, name="sportsetc"), # 기타 스포츠 페이지 메인 URL
    re_path(r'sportsetc/board/(\d+)/$', sportsetc_views.boardlist, name="sportsetc_board"), # 페이지 목록 URL (매개변수는 페이지 번호)
    path('sportsetc/board/', RedirectView.as_view(url='/sports/sportsetc/board/1', permanent=True)), # sportsetc/board/로 접속 시 sportsetc_board로 리다이렉트
    path('sportsetc/board/create/', sportsetc_views.board_create, name="sportsetc_board_create"), # 새 게시물 생성 URL
    re_path(r'sportsetc/board/post/(\d+)/$', sportsetc_views.board_read, name="sportsetc_board_read"), # 게시물 조회 URL (매개변수는 게시물 번호)
    path('sportsetc/board/post/', RedirectView.as_view(url='/sports/sportsetc/board/1', permanent=True)), # sportsetc/board/로 접속 시 sportsetc_board로 리다이렉트
    re_path(r'sportsetc/board/post/(\d+)/update/$', sportsetc_views.board_update, name="sportsetc_board_update"), # 게시물 수정 URL (매개변수는 게시물 번호)
    re_path(r'sportsetc/board/post/(\d+)/delete/$', sportsetc_views.board_delete, name="sportsetc_board_delete"), # 게시물 삭제 URL (매개변수는 게시물 번호)
    re_path(r'sportsetc/board/post/(\d+)/like/$', sportsetc_views.board_like, name="sportsetc_board_like"), # 게시물 좋아요 URL (매개변수는 게시물 번호)
    re_path(r'sportsetc/board/post/(\d+)/dislike/$', sportsetc_views.board_dislike, name="sportsetc_board_dislike"), # 게시물 좋아요 URL (매개변수는 게시물 번호)
    re_path(r'sportsetc/board/post/(\d+)/addreply', sportsetc_views.board_add_reply, name="sportsetc_board_addreply"), # 게시물 댓글 추가 URL (매개변수는 게시물 번호)
    re_path(r'sportsetc/board/post/delreply/(\d+)', sportsetc_views.board_del_reply, name="sportsetc_board_delreply"), # 게시물 댓글 삭제 URL (매개변수는 게시물 번호, 댓글 번호)
    re_path(r'sportsetc/board/post/replylike/(\d+)', sportsetc_views.board_reply_like, name="sportsetc_board_addreply"), # 게시물 댓글 추가 URL (매개변수는 게시물 번호)
    re_path(r'sportsetc/board/post/replydislike/(\d+)', sportsetc_views.board_reply_dislike, name="sportsetc_board_delreply"), # 게시물 댓글 삭제 URL (매개변수는 게시물 번호, 댓글 번호)
]
