from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from main.models import Member
import json
from django.contrib import auth

"""
    @는 '데코레이터' 로서 특정 기능을 추가해주는 코드이다.(자세한 것 서칭하시오)
    @require_http_methods는 허용하는 메서드만 목록으로 지정하는 데코레이터
    @require_GET은 get 메서드에 사용하는 데코레이터
    @require_POST는 post 메서드에 사용하는 데코레이터
    이다. django 5.0 이상부터 사용가능(레퍼런스 가이드 참고)
"""
# Create your views here.
@require_GET
def main(request):
    return render(request, 'main/main.html');

@require_http_methods(["GET", "POST"])
def join(request):
    if request.method == "GET":
        return render(request, 'main/join.html');
    elif request.method == "POST":
        user_id = request.POST["user_id"];
        password = request.POST["password"];
        user_name = request.POST["user_name"];
        phone_num = request.POST["phone_num"];
        email = request.POST["email"];

        Member.objects.create_user(user_id, email, password, user_id=user_id, user_name=user_name, phone_num=phone_num);

        msg = "<script>";
        msg += "alert('회원 가입되었습니다.');";
        msg += f"location.href = '/main/';";
        msg += "</script>";

        return HttpResponse(msg);

@require_POST
def member_id_check(request):
    req = json.loads(request.body);

    try:
        member = Member.objects.get(user_id=req['mbr_id']);
    except:
        member = None;

    if member == None:
        dupl_id_flag = False;
    else:
        dupl_id_flag = True;
        
    content = {
        'dupl_id_flag': dupl_id_flag
    };
        
    return JsonResponse(content);

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return render(request, 'main/login.html');
    elif request.method == "POST":
        user_id = request.POST['user_id'];
        password = request.POST['password'];

        member = auth.authenticate(request, username=user_id, password=password);

        if member is not None:
            auth.login(request, member);
            
            return redirect("/main/");
        else:
            msg = "<script>";
            msg += "alert('로그인 아이디/비밀번호가 틀립니다. 다시 로그인 하세요.');";
            msg += "location.href = '/main/login/';";
            msg += "</script>";

            return HttpResponse(msg);

@require_POST
def logout(request):
    auth.logout(request);

    msg = "<script>";
    msg += "alert('로그아웃 되었습니다.');";
    msg += "location.href = '/main/';";
    msg += "</script>";

    return HttpResponse(msg);