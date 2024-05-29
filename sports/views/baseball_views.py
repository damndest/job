from django.shortcuts import render, redirect, HttpResponse
from . import base_views, board_views

# 야구 메인 페이지 뷰
def baseball(request):
    return render(request, 'sports/baseball.html')

# 야구 게시판 목록 뷰
def boardlist(request, page):
    return board_views.boardlist(request, 'baseball', page)

# 야구 게시글 작성 뷰
def board_create(request):
    return board_views.create(request, 'baseball')

# 야구 게시글 조회 뷰
def board_read(request, post_id):
    return board_views.read(request, 'baseball', post_id)

# 야구 게시글 수정 뷰
def board_update(request, post_id):
    return board_views.update(request, 'baseball', post_id)

# 야구 게시글 삭제 뷰
def board_delete(request, post_id):
    return board_views.delete(request, 'baseball', post_id)
    