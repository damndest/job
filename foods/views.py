from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from main.models import Member
from foods.models import Food, FoodReply
from datetime import datetime
import json
import os
from django.conf import settings
from urllib import parse
import shutil

# 로그인 화면 강제 반환 함수
def return_login():
    msg = "<script>";
    msg += "alert('로그인 후 사용 가능합니다.');";
    msg += "location.href = '/main/login/';";
    msg += "</script>";

    return HttpResponse(msg);

# 음식 지역별 파일 업로드
def file_upload_foods_area(request, food_no):
    dir_name = str(food_no);

    # 파일 경로는 각 팀원마다 다르게 지정(여기는 음식 지역별 이므로 음식 지역별 경로 설정함)
    path = settings.MEDIA_ROOT + "/foods/area/" + dir_name + "/";

    if not os.path.isdir(path):
        # mkdir 은 이미 생성한 폴더가 있으면 오류 발생하므로 makedirs 메서드로 변경
        os.makedirs(path, exist_ok=True);

    for f in request.FILES.getlist("files"):
        upload_file = open(path + str(f), 'wb');

        for chunk in f.chunks():
            upload_file.write(chunk);

# 음식 지역별 파일 제거
def remove_file_foods_area(food_no):
    path = settings.MEDIA_ROOT + "/foods/area/" + str(food_no);

    if os.path.isdir(path):
        shutil.rmtree(path);

@require_GET
def foods_area(request):
    food = Food.objects.all();
    
    content = {
        "food_list": food
    }

    return render(request, 'foods/area/list.html', content);

@require_http_methods(["GET", "POST"])
def add_foods(request):
    if request.method == "GET":
        if request.user.is_active:
            return render(request, 'foods/add.html');
        else:
            return return_login();
    elif request.method == "POST":
        now = datetime.now();

        food = Food(
            writer=request.POST['writer'],
            title=request.POST['title'],
            content=request.POST['content'],
            food_type=request.POST['food_type'],
            area_name=request.POST['area_name'],
            regist_date=now,
            modify_date=now,
            member_idx=Member.objects.get(user_id=request.user)
        );

        food.save();

        file_upload_foods_area(request, food.food_no);

        msg = "<script>";
        msg += "alert('음식 게시글이 저장되었습니다.');";
        msg += f"location.href = '/foods/area/';";
        msg += "</script>";

        return HttpResponse(msg);

@require_GET
def foods_area_detail(request, food_no):
    food = Food.objects.values().get(food_no=food_no);
    food_see_cnt = food['see_cnt'] + 1;

    food_obj = Food.objects.get(food_no=food_no);
    food_obj.see_cnt = food_see_cnt;
    food_obj.save();
    
    reply = FoodReply.objects.filter(food_no=food_no);
    
    if request.user.is_active:
        member = Member.objects.get(member_idx=food['member_idx_id']);

        try:
            file_list = os.listdir(settings.MEDIA_ROOT + "/foods/area/" + str(food_no));
        
            content = {
                "food": food,
                "user_id": member.user_id,
                "reply": reply,
                "member_idx": Member.objects.get(user_id=request.user),
                "file_list": file_list
            };
        except: 
            content = {
                "food": food,
                "user_id": member.user_id,
                "reply": reply,
                "member_idx": Member.objects.get(user_id=request.user)
            };
    else:
        try:
            file_list = os.listdir(settings.MEDIA_ROOT + "/foods/area/" + str(food_no) + "/");
        
            content = {
                "food": food,
                "reply": reply,
                "file_list": file_list
            };
        except:
            content = {
                "food": food,
                "reply": reply
            };

    return render(request, 'foods/area/detail.html', content);

@require_http_methods(["GET", "POST"])
def mod_foods_area(request, food_no):
    if request.method == "GET":
        food = Food.objects.values().get(food_no=food_no);

        req_user = request.user;
        
        if req_user.is_active:
            member = Member.objects.get(member_idx=food['member_idx_id']);
            
            if req_user.username == member.user_id:
                try:
                    file_list = os.listdir(settings.MEDIA_ROOT + "/foods/area/" + str(food_no));
                
                    content = {
                        "food": food,
                        "file_list": file_list
                    };
                except:
                    content = {
                        "food": food
                    };
            
                return render(request, 'foods/area/mod.html', content);
            else:
                msg = "<script>";
                msg += "alert('접근할 수 없는 URL 입니다.');";
                msg += "location.href = '/foods/area/';";
                msg += "</script>";

                return HttpResponse(msg);
        else:
            return return_login();
    elif request.method == "POST":
        food = Food.objects.get(food_no=food_no);

        food.writer = request.POST['writer'];
        food.title = request.POST['title'];
        food.content = request.POST['content'];
        food.area_name = request.POST['area_name'];
        food.modify_date = datetime.now();

        food.save();

        file_upload_foods_area(request, food.food_no);

        msg = "<script>";
        msg += f"alert('{food_no}번 게시글이 수정 되었습니다.');";
        msg += f"location.href = '/foods/area/{food_no}/';";
        msg += "</script>";

        return HttpResponse(msg);

@require_http_methods(["GET", "POST"])
def del_foods_area(request, food_no):
    remove_file_foods_area(food_no);

    # 음식 지역별 댓글은 외래키 on delete가 CASCADE로 지정되어 있기 때문에 따로 삭제하지 않아도 음식 게시판 삭제 시 음식 댓글도 삭제된다.
    Food.objects.get(food_no=food_no).delete();

    msg = "<script>";
    msg += f"alert('{food_no}번 게시글을 삭제 했습니다.');";
    msg += "location.href = '/foods/area/';";
    msg += "</script>";

    return HttpResponse(msg);

@require_POST
def del_chk_foods_area(request):
    req = json.loads(request.body);

    food_list = req['food_list'];

    for food_no in food_list:
        remove_file_foods_area(food_no);
        
        Food.objects.get(food_no=food_no).delete();

    content = {
        'msg': '성공'
    };

    return JsonResponse(content);

@require_POST
def add_rpl_foods_area(request):
    req = json.loads(request.body);

    food_no = req['food_no'];

    reply = FoodReply();
    reply.nickname = req['nickname'];
    reply.content = req['content'];
    reply.food_no = Food.objects.get(food_no=food_no);
    reply.member_idx = Member.objects.get(user_id=request.user);
    reply.regist_date = datetime.now();

    reply.save();

    content = {
        'food_no': food_no
    };

    return JsonResponse(content);

@require_POST
def del_rpl_foods_area(request):
    req = json.loads(request.body);

    FoodReply.objects.get(food_rpl_no=req['food_rpl_no']).delete();

    content = {
        'food_no': req['food_no']
    };

    return JsonResponse(content);

@require_GET
def download_foods_area(request, food_no, file_name):
    file_name = parse.unquote(file_name);
    file_path = os.path.join(settings.MEDIA_ROOT, "foods", "area", str(food_no), file_name);
    
    if os.path.exists(file_path):
        read_file = open(file_path, 'rb');
        response = HttpResponse(read_file.read());
        response['Content-Disposition'] = 'attachment;filename=' + parse.quote(file_name);

        return response;
    else:
        msg = "<script>";
        msg += f"alert('{file_name}의 파일이 존재하지 않습니다.');";
        msg += "history.back();";
        msg += "</script>";

        return HttpResponse(msg);

@require_GET
def del_file_foods_area(request, food_no, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, "foods", "area", str(food_no), file_name);

    os.remove(file_path);

    msg = "<script>";
    msg += f"alert('{file_name} 파일을 삭제했습니다.');";
    msg += f"location.href = '/foods/area/{food_no}/mod/';";
    msg += "</script>";

    return HttpResponse(msg);