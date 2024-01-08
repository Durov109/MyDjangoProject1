from django.urls import path
from . import views as views_days

urlpatterns = [
    path('<int:num_day>', views_days.number_day),
    path('<str:day>', views_days.get_info_day, name='day-week'),
    path('', views_days.index),
    path('monday/', views_days.monday),
    path('tuesday/', views_days.tuesday),
]
