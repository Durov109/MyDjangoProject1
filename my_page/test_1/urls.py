from django.urls import path
from . import views as views_test

urlpatterns = [
    path('', views_test.hello_world),
    path('views/', views_test.views_all_worker),
]
