from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Leo(request):
    return HttpResponse("♌ Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).")

def Cancer(request):
    return HttpResponse("♋ Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).")

def Aries(request):
    return HttpResponse("♈ Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")

def Taurus(request):
    return HttpResponse("♉ Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")

def Gemini(request):
    return HttpResponse("♊ Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")

def Virgo(request):
    return HttpResponse("♍ Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).")

def Libra(request):
    return HttpResponse("♎ Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")

def Scorpio(request):
    return HttpResponse("♏ Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).")

def Sagittarius(request):
    return HttpResponse("♐ Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).")

def Capricorn(request):
    return HttpResponse("♑ Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).")

def Aquarius(request):
    return HttpResponse("♒ Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).")

def Pisces(request):
    return HttpResponse("♓ Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).")