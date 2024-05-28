from django.shortcuts import render, redirect, HttpResponse


# 스포츠 서브앱 메인 화면 뷰 함수
def index(request, page):
    content = {
        'page' : page,
    }
    return render(request, 'sports/index.html', content)

# 스포츠 서브앱 메인 화면 뷰 함수
def create(request):
    return render(request, 'sports/create.html')

def read(request, article_id):
    content = {
        'article_id' : article_id,
    }
    return render(request, 'sports/read.html', content)

def update(request, article_id):
    content = {
        'article_id' : article_id,
    }
    return render(request, 'sports/update.html', content)

def delete(request, article_id):
    content = {
        'article_id' : article_id,
    }
    return render(request, 'sports/delete.html', content)