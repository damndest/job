from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from economy.models import Border   # ***1번 앱폴더이름 주의
import os 
from django.core.paginator import Paginator

# Create your views here.

def financeBoard(request, page):
    border = Border.objects.all().order_by('-id')
    

    # Paginator(데이터, 분할할 데이터 수)
    paging = Paginator(border, 10)
    
    str_page = str(page)
    # 맨 마지막 숫자
    last = int(str_page[-1])
    first = int(str_page[:-1] + '1')

    if last == 0:
        max = first
        first = max - 10
    elif first + 10 > paging.num_pages:
        max = paging.num_pages + 1
    else :
        max = first + 10
    page_num = range(first, max)


    try:
        content = {
            'border':paging.page(page),
            'page_num':page_num,
        }
    except:
        content = {
            'border' : paging.page(paging.num_pages),
            'page_num' : page_num,
        }    

    return render(request, 'economy/financeboard.html', content);

def financeMain(request):
    return render(request, 'economy/financeboard.html');

def boardAdd(request):
    if request.method == 'POST':
        now = datetime.now()
        border = Border()
        border.title = request.POST['title']
        border.contents = request.POST.get("contents");
        border.writer = request.user.username;
        border.writetime = now
        border.updatetime = now
        border.hits = request.POST['hits']
        border.save()

        msg = "<script>";
        msg += "alert('게시글이 저장되었습니다.');";
        msg += f"location.href='/economy/financeboard/1';";
        msg += "</script>";
        return HttpResponse(msg);
        # return redirect('BD', border.id)
        # return render(request, 'border/detail.html')
    else: # GET 방식
        if request.user.is_active:
            return render(request, 'economy/boardadd.html');
        else:
            msg = "<script>"
            msg += "alert('로그인 후 이용이 가능합니다.');"
            # msg += "location.href='/account/login/';"
            msg += "</script>"
            return HttpResponse(msg)

    # return render(request, 'economy/boardadd.html');

def boardDetail(request, borderId):
    if request.user.is_active :
        border = Border.objects.values().get(id=borderId);
        # Border.objects.filter(id=borderId).update(조회수 = border['조회수'] + 1)
        # get(id=고유번호)
        # filter(컬럼명 = 값)
        # reply = Reply.objects.filter(border_id=borderId).values()
        
        try:
            # dirList = os.listdir(settings.MEDIA_ROOT + "/" + str(borderId))

            content = {
                'border':border,
                # 'reply':reply,
                # 'dirList':dirList,
            }
        except:
            content = {
            'border' : border,
            # 'reply':reply,
            }
        return render(request, 'economy/boarddetail.html', content);
    else:
        msg = "<script>";
        msg += "alert('로그인 후 사용 가능합니다.');"
        msg += "location.href='/economy/financeboard/';"
        msg += "</script>"
        return HttpResponse(msg);




    # return render(request, 'economy/boarddetail.html');

def boardDelete(request, borderId):
    # path = settings.MEDIA_ROOT + "/" + str(borderId) + "/"
    # if os.path.isdir(path):
        # dirList = os.listdir(path)
        # for f in dirList:
        #     os.remove(path + "/" + f)
        # os.rmdir(path)
        # shutil.rmtree(path)

    Border.objects.get(id=borderId).delete()
    # Reply.objects.filter(border_id=borderId).delete()
    content = {
        'borderId':borderId
    }
    return render(request, 'border/delete.html', content);


def financeQuiz(request):
    return render(request, 'economy/financequiz.html');
def domestic(request):
    return render(request, 'economy/financemain.html');
def financeCondition(request):
    return render(request, 'economy/financecondition.html');

