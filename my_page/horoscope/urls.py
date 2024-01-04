from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    # path('leo/', views_horoscope.Leo),
    # path('oven/', views_horoscope.Aries),
    # path('vodoley/', views_horoscope.Aquarius),
    # path('rak/', views_horoscope.Cancer),
    # path('kozerog/', views_horoscope.Capricorn),
    # path('bliznesy/', views_horoscope.Gemini),
    # path('vesy/', views_horoscope.Libra),
    # path('scorpion/', views_horoscope.Scorpio),
    # path('streles/', views_horoscope.Sagittarius),
    # path('teles/', views_horoscope.Taurus),
    # path('ryby/', views_horoscope.Pisces),
    # динамический роут
    path('<sign_zodiac>/', views_horoscope.get_info_about_sign_zodiac),
]
