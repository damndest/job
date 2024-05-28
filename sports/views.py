from django.shortcuts import render, redirect, HttpResponse


# 스포츠 서브앱 메인 화면 뷰 함수
def index(request):
    return render(request, 'sports/index.html')

def pagelist(request):
    return render(request, 'sports/pagelist.html')

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

def f_pagelist(request):
    return pagelist(request)

def f_create(request):
    return create(request)

def f_read(request, article_id):
    return read(request, article_id)

def f_update(request, article_id):
    return update(request, article_id)

def f_delete(request, article_id):
    return update(request, article_id)

def b_pagelist(request):
    return pagelist(request)

def b_create(request):
    return create(request)

def b_read(request, article_id):
    return read(request, article_id)

def b_update(request, article_id):
    return update(request, article_id)

def b_delete(request, article_id):
    return update(request, article_id)

def e_pagelist(request):
    return pagelist(request)

def e_create(request):
    return create(request)

def e_read(request, article_id):
    return read(request, article_id)

def e_update(request, article_id):
    return update(request, article_id)

def e_delete(request, article_id):
    return update(request, article_id)

