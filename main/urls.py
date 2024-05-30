from django.urls import path
from . import views

app_name = "main";

urlpatterns = [
    path('', views.main),
    path('join/', views.join, name="join"),
    path('join/member_id_check/', views.member_id_check, name="mid_chk"),
    path('login/', views.login, name="login"),
]
