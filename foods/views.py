from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse
from foods.models import Member, Food
from datetime import datetime

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
            msg = "<script>";
            msg += "alert('로그인 후 사용 가능합니다.');";
            msg += "location.href = '/main/login/';";
            msg += "</script>";

            return HttpResponse(msg);
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

        msg = "<script>";
        msg += "alert('음식 게시글이 저장되었습니다.');";
        msg += f"location.href = '/foods/area/';";
        msg += "</script>";

        return HttpResponse(msg);

@require_GET
def foods_area_detail(request, food_no):
    food = Food.objects.values().get(food_no=food_no);
    
    if request.user.is_active:
        member = Member.objects.values().get(member_idx=food['member_idx_id']);
        
        content = {
            "food": food,
            "user_id": member["user_id"]
        };
    else:
        content = {
            "food": food
        };

    return render(request, 'foods/area/detail.html', content);