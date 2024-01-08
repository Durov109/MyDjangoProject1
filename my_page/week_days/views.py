from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    result = '''<h1>Список дел</h1>
                <url>
                    <li><a href='monday/'>Понедельник</a></li>
                    <li><a href='tuesday/'>Вторник</a></li>
                </url>
             '''
    return HttpResponse(result)


def monday(request):
    result = '''<h1>Список дел на понедельник</h1>
                <p>
                    Понедельник день тяжелый </li>
                </p>
                <p>
                    <a href="/week_days">Главная</a>
                </p>
             '''
    return HttpResponse(result)


def tuesday(request):
    result = '''<h1>Список дел на вторник</h1>
                <p>
                    <li> сериалы </li>
                    <li> кушать </li>
                    <li> отдыхать </li>
                </p>
                <p>
                    <a href="/week_days">Главная</a>
                </p>
             '''
    return HttpResponse(result)

def get_info_day(request, day):
    if day == 'monday':
        return monday(request)
    elif day == 'tuesday':
        return tuesday(request)
    


def number_day(request, num_day: int):
    day_dict = {1: 'monday/', 2: 'tuesday/', 3: 'wednesday/',
                4: 'thursday/', 5: 'friday/', 6: 'saturday/', 7: 'sunday/'}
    
    if day_dict.get(num_day, None):
        get_day = day_dict[num_day]
        redirect_url = reverse('day-week', args=(get_day, ))
        return HttpResponsePermanentRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неверный номер дня недели - {num_day}")
