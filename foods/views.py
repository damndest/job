from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from foods.models import Food

@require_GET
def foods_area(request):
    food = Food.objects.all();

    content = {
        "food_list": food
    }

    return render(request, 'foods/area/list.html', content);