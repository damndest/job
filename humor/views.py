from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .models import Post

def index(request):
    return render(request, 'humor/domestic.html')

def domestic(request):
    posts = [
        {'title': '첫 번째 국내 유머', 'content': '첫 번째 국내 유머입니다.'},
        {'title': '두 번째 국내 유머', 'content': '두 번째 국내 유머입니다.'},
        {'title': '세 번째 국내 유머', 'content': '세 번째 국내 유머입니다.'},
    ]
    return render(request, 'humor/domestic.html', {'posts': posts})

def international_index(request):
    return render(request, 'humor/international.html')

def international(request):
    posts = [
        {'title': '첫 번째 외국 유머', 'content': '첫 번째 외국 유머입니다.'},
        {'title': '두 번째 외국 유머', 'content': '두 번째 외국 유머입니다.'},
        {'title': '세 번째 외국 유머', 'content': '세 번째 외국 유머입니다.'},
    ]
    return render(request, 'humor/international.html', {'posts': posts})

def post_detail(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    post.views += 1
    post.save()
    return render(request,'humor/post_detail.html', {'post': post})

def write_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')

        post = Post(
            title=title,
            content=content,
            image=image,
            author=request.user
        )
        post.save()

        return redirect('domestic')
    return render(request, 'humor/write_post.html')

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('post_detail', post_id=post_id)

def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.dislikes += 1
    post.save()
    return redirect('post_detail', post_id=post_id)
