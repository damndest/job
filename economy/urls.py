from django.urls import path, re_path
from . import views

app_name="BD"

urlpatterns = [
    re_path(r'financeboard/(\d+)/$', views.financeBoard, name='FB'),
    path('financemain/', views.financeMain, name='FM'),
    path('boardadd/', views.boardAdd, name='FBBA'),
    re_path(r'boarddetail/(\d+)/$', views.boardDetail, name='FBBDTL'),
    re_path(r'boarddelete/(\d+)/$', views.boardDelete, name='FBBDEL'),
    path('financequiz/', views.financeQuiz, name='FQ'),
    path('domestic/', views.domestic, name='FD'),
    path('financerecent/', views.financeCondition, name='FR'),
]
