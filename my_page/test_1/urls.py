from django.urls import path
from . import views as views_test

urlpatterns = [
    path('', views_test.hello_world),
]
