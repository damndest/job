from django.urls import path
from . import views

app_name = "foods";

urlpatterns = [
    path('area/list/<int:page>/', views.foods_area, name='area'),
    path('area/<int:food_no>/', views.foods_area_detail, name='area_detail'),
    path('area/<int:food_no>/mod/', views.mod_foods_area, name='mod_area'),
    path('area/<int:food_no>/del/', views.del_foods_area, name='del_area'),
    path('area/download/<int:food_no>/<str:file_name>', views.download_foods_area, name='download_area'),
    path('area/del_file/<int:food_no>/<str:file_name>/', views.del_file_foods_area),
    path('area/del_chk_list/', views.del_chk_foods_area, name='del_chk_area'),
    path('area/reply/add/', views.add_rpl_foods_area, name='add_rpl_area'),
    path('area/reply/del/', views.del_rpl_foods_area, name='del_rpl_area'),
    path('add/', views.add_foods, name='add'),
]
