from django.shortcuts import render, redirect, HttpResponse
from sports.models import BaseballPost, BaseballPostComment
from datetime import datetime
from django.core.paginator import Paginator
from django.core.exceptions import *

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

# 각 게임별 게시판 테이블 불러오기 위한 딕셔너리
posts = {
    'baseball' : BaseballPost,
}

# 각 게임별 댓글 테이블 불러오기 위한 딕셔너리
comments = {
    'baseball' : BaseballPostComment,
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


# --------------------- 실제 뷰 함수 ---------------------

# 자유게시판 글 목록 뷰 함수
def boardlist(request, game, page):
    post = posts[game].objects.all().order_by('-id')
    # 페이징 설정 부분
    paging = Paginator(post, POST_PER_PAGE)
    page_num = get_page_num(page, paging)
    try:
        board = paging.page(page)
    except:
        board = paging.page(paging.num_pages)
    print(board)
    content = {
        'game' : game,
        'gamename' : gamename[game],
        'page' : page,
        'post' : board,
        'page_num' : page_num,
        'comment' : comments[game].objects.all().order_by('-id'),
    }
    return render(request, 'sports/board/pagelist.html', content)


# 자유게시판 글 작성 뷰 함수
def create(request, game):
    # ! 추후 user.is_active 적용 필요
    if request.user.is_active:
        if request.method == 'GET':
            content = {
                'game' : game,
                'gamename' : gamename[game],
            }
            return render(request, 'sports/board/pagecreate.html', content)
        
        elif request.method == 'POST':
            now = datetime.now()
            post = posts[game]()
            post.title = request.POST['title']
            post.content = request.POST.get('content')
            post.author = request.user.username
            post.wdate = now
            post.udate = now
            post.views = 0
            post.comment = 0
            post.save()

            msg = "<script>"
            msg += "alert('게시글이 저장되었습니다.');"
            msg += f"location.href='/sports/{game}/board/post/{post.id}';"
            msg += "</script>"
            return HttpResponse(msg)
    else:
        return redirect('/sports/forbidden')

# 자유게시판 글 조회 뷰 함수
def read(request, game, post_id):
    try:
        post = posts[game].objects.get(id=post_id)
        post.views += 1
        post.save()
        content = {
            'game' : game,
            'post' : post,
        }
        return render(request, 'sports/board/pageread.html', content)
    except ObjectDoesNotExist as e: # 이미 삭제되었거나 없는 게시물 조회 시
        msg = "<script>"
        msg += f"alert('이미 삭제되었거나 존재하지 않는 게시물입니다.');"
        msg += f"location.href='/sports/{game}/board/1';"
        msg += "</script>"
        return HttpResponse(msg)
    except Exception as e:
        msg = "<script>"
        msg += f"alert('알 수 없는 오류가 발생했습니다.');"
        msg += f"location.href='/sports/{game}/board/1';"
        msg += "</script>"
        return HttpResponse(msg)
    
# 자유게시판 글 수정 뷰 함수
def update(request, game, post_id):
    try:
        post = posts[game].objects.get(id=post_id)
        if request.user.username == post.author:
            if request.method == 'GET':
                content = {
                    'game' : game,
                    'post' : post,
                }
                return render(request, 'sports/board/pageupdate.html', content)
            elif request.method == 'POST':
                post = posts[game].objects.get(id=post_id)
                post.title = request.POST.get('title')
                post.content = request.POST.get('content')
                post.udate = datetime.now()
                post.save()

                msg = "<script>"
                msg += f"alert('게시글이 수정되었습니다.');"
                msg += f"location.href='/sports/{game}/board/post/{post.id}';"
                msg += "</script>"
                return HttpResponse(msg)
        else:
            return redirect('/sports/forbidden')
    except ObjectDoesNotExist as e: # 이미 삭제되었거나 없는 게시물 조회 시
        msg = "<script>"
        msg += f"alert('이미 삭제되었거나 존재하지 않는 게시물입니다.');"
        msg += f"location.href='/sports/{game}/board/1';"
        msg += "</script>"
        return HttpResponse(msg)
    except Exception as e:
        msg = "<script>"
        msg += f"alert('알 수 없는 오류가 발생했습니다.');"
        msg += f"location.href='/sports/{game}/board/1';"
        msg += "</script>"
        return HttpResponse(msg)

# 자유게시판 글 삭제 뷰 함수
def delete(request, game, post_id):
    try:
        post = posts[game].objects.get(id=post_id)
        if request.user.username == post.author:
            post = posts[game].objects.get(id=post_id)
            post.delete()

            msg = "<script>"
            msg += f"alert('게시글이 삭제되었습니다.');"
            msg += f"location.href='/sports/{game}/board/1';"
            msg += "</script>"
            return HttpResponse(msg)
        
        else:
            return redirect('/sports/forbidden')
    except ObjectDoesNotExist as e:  # 이미 삭제되었거나 없는 게시물 조회 시
        msg = "<script>"
        msg += f"alert('이미 삭제되었거나 존재하지 않는 게시물입니다.');"
        msg += f"location.href='/sports/{game}/board/1';"
        msg += "</script>"
        return HttpResponse(msg)
    except Exception as e:
        msg = "<script>"
        msg += f"alert('알 수 없는 오류가 발생했습니다.');"
        msg += f"location.href='/sports/{game}/board/1';"
        msg += "</script>"
        return HttpResponse(msg)