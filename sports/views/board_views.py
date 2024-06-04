from django.shortcuts import render, redirect, HttpResponse
from main.models import Member
from sports.models import SportsPost, SportsReply
from datetime import datetime
from django.core.paginator import Paginator
from django.http import Http404
from django.core.exceptions import *
import logging

logger = logging.getLogger(__name__)

# sports 서브앱의 자유게시판에서 공통적으로 사용될 뷰 함수 묶음 파일
# 어떤 종목의 자유게시판인지는 매개변수로 들어오는 game 문자열을 통해 결정
# (ex. game 매개변수가 'baseball'일 경우 자동으로 야구 관련 테이블을 불러와서 자동으로 파라미터로 보내줌)

POST_PER_PAGE = 10 # 게시판 페이지 별 표시할 페이지 수 (1페이지 당 10개의 게시물 표시)

# 영문 게임명 -> 한글 게임명 변환하기 위한 딕셔너리
gamename = {
    'baseball' : "야구",
    'football' : "축구",
    'sportsetc' : "기타 스포츠",
}

# 현재 페이지(page)의 소속 범위를 range()로 출력하는 함수
# ex : 현재 페이지(page)가 '5'이면 range(1, {POST_PER_PAGE(10)})을 출력
# boardlist 안에 있어도 되는데 그냥 보기 흉해서 따로 빼서 구현
def get_page_num(page:str, paging:Paginator) -> range:
    if int(page) > paging.num_pages:
        page = str(paging.num_pages)
    str_page = str(page)
    last = int(str_page[-1])
    first = int(str_page[:-1] + '1')

    if last == 0:
        max = first
        first = max - POST_PER_PAGE
    elif first + POST_PER_PAGE > paging.num_pages:
        max = paging.num_pages + 1
    else:
        max = first + POST_PER_PAGE

    return range(first, max)

# 로그인 요청하는 함수
def need_login() -> HttpResponse:
    msg = "<script>"
    msg += "alert('로그인 후 이용하세요.');"
    msg += f"location.href='/main/login';"
    msg += "</script>"
    return HttpResponse(msg)

# 존재하지 않는 게시물 접근시 처리하는 함수
def invalid_board(game:str) -> HttpResponse:
    msg = "<script>"
    msg += f"alert('이미 삭제되었거나 존재하지 않는 게시물입니다.');"
    msg += f"location.href='/sports/{game}/board/1';"
    msg += "</script>"
    return HttpResponse(msg)

# 존재하지 않는 댓글 접근시 처리하는 함수
def invalid_reply() -> HttpResponse:
    msg = "<script>"
    msg += f"alert('댓글이 존재하지 않습니다.');"
    msg += f"location.href='javascript:history.back()';"
    msg += "</script>"
    return HttpResponse(msg)

# 기타 오류 발생 시
def unknown_error(game:str) -> HttpResponse:
    msg = "<script>"
    msg += f"alert('알 수 없는 오류가 발생했습니다.');"
    msg += f"location.href='/sports/{game}/board/1';"
    msg += "</script>"
    return HttpResponse(msg)

# --------------------- 실제 뷰 함수 ---------------------

# 자유게시판 글 목록 뷰 함수
def boardlist(request, game, page):
    post_list = SportsPost.objects.filter(post_game=game).order_by('-post_id').values('post_id', 'post_title', 'post_author', 'post_author_nn', 'post_views')

    for post in post_list:
        post_id = post['post_id']
        post['reply_count'] = SportsPost.objects.get(post_id=post_id).post_reply.count()
        post['like_count'] = SportsPost.objects.get(post_id=post_id).post_like.count()
        post['dislike_count'] = SportsPost.objects.get(post_id=post_id).post_dislike.count()
    # 페이징 설정 부분
    paging = Paginator(post_list, POST_PER_PAGE)
    page_num = get_page_num(page, paging)
    try:
        board = paging.page(page)
    except:
        board = paging.page(paging.num_pages)
    content = {
        'game' : game,
        'gamename' : gamename[game],
        'page' : page,
        'post' : board,
        'page_num' : page_num,
    }
    return render(request, 'sports/board/postlist.html', content)


# 자유게시판 글 작성 뷰 함수
def create(request, game):
    # ! 추후 user.is_active 적용 필요
    if request.user.is_active:
        if request.method == 'GET':
            content = {
                'game' : game,
                'gamename' : gamename[game],
            }
            return render(request, 'sports/board/postcreate.html', content)
        
        elif request.method == 'POST':
            now = datetime.now()
            post = SportsPost()
            post.post_title = request.POST.get('title')
            post.post_game = game
            post.post_author = request.user.user_id
            if request.POST.get('author') == None:
                post.post_author_nn = request.user.user_id
            else:
                post.post_author_nn = request.POST.get('author')
            post.post_content = request.POST.get('content')
            post.post_wdate = now
            post.post_udate = now
            post.post_views = 0
            post.post_member = request.user
            post.save()

            msg = "<script>"
            msg += "alert('게시글이 저장되었습니다.');"
            msg += f"location.href='/sports/{game}/board/post/{post.post_id}';"
            msg += "</script>"
            return HttpResponse(msg)
    else:
        return need_login()

# 자유게시판 글 조회 뷰 함수
def read(request, game, post_id):
    try:
        post = SportsPost.objects.get(post_id=post_id)
        reply = SportsReply.objects.filter(post_id=post_id)
        post.post_views += 1
        post.save()
        content = {
            'game' : game,
            'post' : post,
            'gamename' : gamename[game],
            'reply' : reply,
        }
        return render(request, 'sports/board/postread.html', content)
    except ObjectDoesNotExist as e: # 이미 삭제되었거나 없는 게시물 조회 시
        return invalid_board(game)
    except Exception as e:
        print(e)
        return unknown_error(game)
    
# 자유게시판 글 수정 뷰 함수
def update(request, game, post_id):
    try:
        post = SportsPost.objects.get(post_id=post_id)
        if request.user == post.post_member:
            if request.method == 'GET':
                content = {
                    'game' : game,
                    'post' : post,
                    'gamename' : gamename[game],
                }
                return render(request, 'sports/board/postupdate.html', content)
            elif request.method == 'POST':
                post.post_title = request.POST.get('title')
                post.post_content = request.POST.get('content')
                post.post_udate = datetime.now()
                post.save()

                msg = "<script>"
                msg += f"alert('게시글이 수정되었습니다.');"
                msg += f"location.href='/sports/{game}/board/post/{post.post_id}';"
                msg += "</script>"
                return HttpResponse(msg)
        else:
            return redirect('/sports/forbidden')
    except ObjectDoesNotExist as e: # 이미 삭제되었거나 없는 게시물 조회 시
        return invalid_board(game)
    except Exception as e:
        return unknown_error(game)

# 자유게시판 글 삭제 뷰 함수
def delete(request, game, post_id):
    try:
        post = SportsPost.objects.get(post_id=post_id)
        if request.user == post.post_member:
            post.delete()

            msg = "<script>"
            msg += f"alert('게시글이 삭제되었습니다.');"
            msg += f"location.href='/sports/{game}/board/1';"
            msg += "</script>"
            return HttpResponse(msg)
        
        else:
            return redirect('/sports/forbidden')
    except ObjectDoesNotExist as e:  # 이미 삭제되었거나 없는 게시물 조회 시
        return invalid_board(game)
    except Exception as e:
        return unknown_error(game)
    
# 자유게시판 글 좋아요 뷰 함수
def like(request, game, post_id):
    try:
        if request.user.is_active:
            post = SportsPost.objects.get(post_id=post_id)
            if request.user == post.post_member:
                msg = "<script>"
                msg += f"alert('자신의 게시글에 좋아요를 설정할 수 없습니다.');"
                msg += f"location.href='/sports/{game}/board/post/{post.post_id}';"
                msg += "</script>"
                return HttpResponse(msg)
            else:
                if post.post_like.filter(member_idx=request.user.member_idx).exists():
                    msg = "<script>"
                    msg += f"alert('이미 좋아요가 설정된 게시물입니다.');"
                    msg += f"location.href='/sports/{game}/board/post/{post.post_id}';"
                    msg += "</script>"
                    return HttpResponse(msg)
                else:
                    post.post_like.add(request.user)
                    return redirect(f'/sports/{game}/board/post/{post.post_id}')
        else:
            return need_login()

    except ObjectDoesNotExist as e:  # 이미 삭제되었거나 없는 게시물 조회 시
        return invalid_board(game)
    except Exception as e:
        return unknown_error(game)
    

# 자유게시판 글 싫어요 뷰 함수
def dislike(request, game, post_id):
    try:
        if request.user.is_active:
            post = SportsPost.objects.get(post_id=post_id)
            if request.user == post.post_member:
                msg = "<script>"
                msg += f"alert('자신의 게시글에 싫어요를 설정할 수 없습니다.');"
                msg += f"location.href='/sports/{game}/board/post/{post.post_id}';"
                msg += "</script>"
                return HttpResponse(msg)
            else:
                print(post.post_like.all())
                if post.post_dislike.filter(member_idx=request.user.member_idx).exists():
                    msg = "<script>"
                    msg += f"alert('이미 싫어요가 설정된 게시물입니다.');"
                    msg += f"location.href='/sports/{game}/board/post/{post.post_id}';"
                    msg += "</script>"
                    return HttpResponse(msg)
                else:
                    post.post_dislike.add(request.user)
                    return redirect(f'/sports/{game}/board/post/{post.post_id}')
        else:
            return need_login()

    except ObjectDoesNotExist as e:  # 이미 삭제되었거나 없는 게시물 조회 시
        return invalid_board(game)
    except Exception as e:
        return unknown_error(game)

# 자유 게시판 댓글 작성 뷰 함수
def add_reply(request, game, post_id):
    if request.method == 'POST':
        try:
            if request.user.is_active:
                reply = SportsReply()
                reply.reply_author = request.user.user_id
                if request.POST.get('author') == None:
                    reply.reply_author_nn = request.user.user_id
                else:
                    reply.reply_author_nn = request.POST.get('author')
                reply.reply_content = request.POST.get('reply')
                reply.reply_wdate = datetime.now()
                reply.post_id = SportsPost.objects.get(post_id=post_id)
                reply.reply_member = request.user
                reply.save()
                return redirect(f'/sports/{game}/board/post/{post_id}')
            else:
                return need_login()
        except ObjectDoesNotExist as e:  # 이미 삭제되었거나 없는 게시물 조회 시
            return invalid_board(game)
        except Exception as e:
            print(e)
            return unknown_error(game)
    else:
        return invalid_board(game)

# 자유게시판 댓글 삭제 뷰 함수
def del_reply(request, game, reply_id):
    try:
        reply = SportsReply.objects.get(reply_id=reply_id)
        if request.user == reply.reply_member:
            post_id = reply.post_id.post_id
            reply.delete()
            msg = "<script>"
            msg += "alert('댓글이 삭제되었습니다.');"
            msg += f"location.href='/sports/{game}/board/post/{post_id}';"
            msg += "</script>"
            return HttpResponse(msg)
        else:
            return redirect('/sports/forbidden')
    except ObjectDoesNotExist as e:  # 이미 삭제되었거나 없는 게시물 조회 시
        print(e)
        return invalid_reply()
    except Exception as e:
        print(e)
        return unknown_error(game)
    

# 자유게시판 댓글 좋아요 뷰 함수
def reply_like(request, game, reply_id):
    try:
        if request.user.is_active:
            reply = SportsReply.objects.get(reply_id=reply_id)
            if request.user == reply.reply_member:
                msg = "<script>"
                msg += f"alert('자신의 댓글에 좋아요를 설정할 수 없습니다.');"
                msg += f"location.href='/sports/{game}/board/post/{reply.post_id.post_id}';"
                msg += "</script>"
                return HttpResponse(msg)
            else:
                if reply.reply_like.filter(member_idx=request.user.member_idx).exists():
                    msg = "<script>"
                    msg += f"alert('이미 좋아요를 설정하신 댓글입니다.');"
                    msg += f"location.href='/sports/{game}/board/post/{reply.post_id.post_id}';"
                    msg += "</script>"
                    return HttpResponse(msg)
                else:
                    reply.reply_like.add(request.user)
                    return redirect(f'/sports/{game}/board/post/{reply.post_id.post_id}')
        else:
            return need_login()

    except ObjectDoesNotExist as e:  # 이미 삭제되었거나 없는 게시물 조회 시
        return invalid_board(game)
    except Exception as e:
        return unknown_error(game)
    
# 자유게시판 댓글 싫어요 뷰 함수
def reply_dislike(request, game, reply_id):
    try:
        if request.user.is_active:
            reply = SportsReply.objects.get(reply_id=reply_id)
            if request.user == reply.reply_member:
                msg = "<script>"
                msg += f"alert('자신의 댓글에 싫어요를 설정할 수 없습니다.');"
                msg += f"location.href='/sports/{game}/board/post/{reply.post_id.post_id}';"
                msg += "</script>"
                return HttpResponse(msg)
            else:
                if reply.reply_dislike.filter(member_idx=request.user.member_idx).exists():
                    msg = "<script>"
                    msg += f"alert('이미 싫어요를 설정하신 댓글입니다.');"
                    msg += f"location.href='/sports/{game}/board/post/{reply.post_id.post_id}';"
                    msg += "</script>"
                    return HttpResponse(msg)
                else:
                    reply.reply_dislike.add(request.user)
                    return redirect(f'/sports/{game}/board/post/{reply.post_id.post_id}')
        else:
            return need_login()

    except ObjectDoesNotExist as e:  # 이미 삭제되었거나 없는 게시물 조회 시
        return invalid_board(game)
    except Exception as e:
        return unknown_error(game)