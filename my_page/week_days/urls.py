from django.urls import path
from . import views as views_days

urlpatterns = [
    path('', views_days.index),
    path('monday/', views_days.monday),
    path('tuesday/', views_days.tuesday),
    path('<int:num_day>', views_days.number_day),
]
