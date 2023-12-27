from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


def number_day(request, num_day: int):
    day_dict = {1: 'monday', 2: 'tuesday', 3: 'wednesday',
                4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday'}
    if num_day in (1, 2, 3, 4, 5, 6, 7):
        return HttpResponseRedirect(f"{day_dict[num_day]}")
    else:
        return HttpResponseNotFound(f"Неверный номер дня недели - {num_day}")
