from django.urls import path
from . import views

app_name = "food";

urlpatterns = [
    path('area/', views.foods_area, name='area'),
]
