from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index),
    path('type', views_horoscope.list_type_zodiac),
    path('type/<str:type_elem>', views_horoscope.group_zodiac, name='element'),
    # конвертируемый роут (int)
    path('<int:sign_zodiac>/', views_horoscope.get_info_number),
    # динамический роут
    path('<str:sign_zodiac>/', views_horoscope.get_info_about_sign_zodiac, name='horoscope-name'),
]
