from django.urls import path
from . import views

app_name = "foods";

urlpatterns = [
    path('area/<int:food_no>/', views.foods_area_detail, name='area_detail'),
    path('area/<int:food_no>/mod/', views.mod_foods_area, name='mod_area'),
    path('area/', views.foods_area, name='area'),
    path('add/', views.add_foods, name='add'),
]
