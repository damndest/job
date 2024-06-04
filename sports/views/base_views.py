from django.shortcuts import render, redirect, HttpResponse

# sports 서브앱에 사용될 기본(공통) 뷰 함수 묶음 파일

# 영문 게임명 -> 한글 게임명 변환하기 위한 딕셔너리
gamename = {
    'baseball' : "야구",
    'football' : "축구",
    'sportsetc' : "기타 스포츠",
}

# 스포츠 서브앱 메인 인덱스 페이지 뷰 함수
def index(request):
    return render(request, 'sports/index.html')

def gamepage(request, game):
    content = {
        'game' : game,
        'gamename' : gamename[game],
    }
    return render(request, 'sports/game.html', content)


# 접근 경로가 잘못되었을 시 호출될 Forbidden 뷰 함수
def forbidden(request):
    return render(request, 'sports/forbidden.html')
