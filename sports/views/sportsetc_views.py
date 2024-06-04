from django.shortcuts import render, redirect, HttpResponse
from . import base_views, board_views

# 축구 메인 페이지 뷰
def sportsetc(request):
    return base_views.gamepage(request, 'sportsetc')

# 축구 게시판 목록 뷰
def boardlist(request, page):
    return board_views.boardlist(request, 'sportsetc', page)

# 축구 게시글 작성 뷰
def board_create(request):
    return board_views.create(request, 'sportsetc')

# 축구 게시글 조회 뷰
def board_read(request, post_id):
    return board_views.read(request, 'sportsetc', post_id)

# 축구 게시글 수정 뷰
def board_update(request, post_id):
    return board_views.update(request, 'sportsetc', post_id)

# 축구 게시글 삭제 뷰
def board_delete(request, post_id):
    return board_views.delete(request, 'sportsetc', post_id)

# 축구 게시글 좋아요 뷰
def board_like(request, post_id):
    return board_views.like(request, 'sportsetc', post_id)

# 축구 게시글 싫어요 뷰
def board_dislike(request, post_id):
    return board_views.dislike(request, 'sportsetc', post_id)

# 축구 게시글 댓글 작성 뷰
def board_add_reply(request, post_id):
    return board_views.add_reply(request, 'sportsetc', post_id)

# 축구 게시글 댓글 삭제 뷰
def board_del_reply(request, reply_id):
    return board_views.del_reply(request, 'sportsetc', reply_id)

def board_reply_like(request, reply_id):
    return board_views.reply_like(request, 'sportsetc', reply_id)

def board_reply_dislike(request, reply_id):
    return board_views.reply_dislike(request, 'sportsetc', reply_id)