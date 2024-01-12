from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.urls import reverse

class Sign_Group():
    '''Класс формирующий группу знаков по их стихии'''
    
    def __init__(self, nature) -> None:
        self.nature = nature
 
    def get_group(self):
        if self.nature in type_zodiac:
            zod_elem = ""
            for value in type_zodiac[self.nature]:
                redirect_path = reverse('horoscope-name', args=(value, ))
                zod_elem += f"<li> <a href='{redirect_path}'> {value.title()} </a> </li>"
        
            template = f"""
            <ul>
                {zod_elem}
            </ul>
            """
        return HttpResponse(template)

def index(request):
    '''
    Главное меню отображающая знаки зодиака и ссылки на их описание
    
    '''
    zodiacs = list(zodiac_number)
    li_elements = ""
    for sing in zodiacs:
        redirect_path = reverse('horoscope-name', args=(sing, ))
        li_elements += f"<li> <a href='{redirect_path}'>{sing.title()} </a> </li>"

    tempalate = f"""
    <ol>
        {li_elements}
    </ol>
    """
    return HttpResponse(tempalate)


def list_type_zodiac(request):
    '''
    Функция которая выводит список знаков по стихиям и ссылками на них
    '''
    li_elements = ""
    for key in type_zodiac:
        redirect_path = reverse('element', args=(key, ))
        li_elements += f"<li> <a href='{redirect_path}'> {key.title()} </a> </li>"

    template = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(template)

def group_zodiac(request, type_elem):
    '''
    Функция которая обрабатывает динамический роут из фунции list_type_zodiac
    Ищет соотвествия и выводит список знаков которые относятся к стихии 
    '''
    # Присваеваем в переменной класс, а к классу динамический роут
    step_1 = Sign_Group(type_elem)
    # Возвращаем певеменную где указали какую функцию в классе нужно выполнить
    return step_1.get_group()


def get_info_about_sign_zodiac(request, sign_zodiac):
    '''
    Функция которая обрабатывает динамические роуты
    '''
    if sign_zodiac == 'leo':
        return HttpResponse("♌ Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).")
    elif sign_zodiac == 'cancer':
        return HttpResponse("♋ Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).")
    elif sign_zodiac == 'aries':
        return HttpResponse("♈ Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")
    elif sign_zodiac == 'taurus':
        return HttpResponse("♉ Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")
    elif sign_zodiac == 'gemini':
        return HttpResponse("♊ Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")
    elif sign_zodiac == 'virgo':
        return HttpResponse("♍ Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).")
    elif sign_zodiac == 'libra':
        return HttpResponse("♎ Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")
    elif sign_zodiac == 'scorpio':
        return HttpResponse("♏ Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).")
    elif sign_zodiac == 'sagittarius':
        return HttpResponse("♐ Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).")
    elif sign_zodiac == 'capricorn':
        return HttpResponse("♑ Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).")
    elif sign_zodiac == 'aquarius':
        return HttpResponse("♒ Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).")
    elif sign_zodiac == 'pisces':
        return HttpResponse("♓ Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).")
    else: 
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")
    
def get_info_number(request, sign_zodiac: int):
    '''
    Функция которая обрабатывает конвертируемый роут 
    И использует перенаправление HttpResponsePermanentRedirect
    '''
    step1 = list(zodiac_number)
    
    if sign_zodiac > len(step1):
        return HttpResponseNotFound(f"Такого знака зодика нету - {sign_zodiac}, их всего 12")
    else:
        name_zodiac = step1[sign_zodiac-1]
        redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
        return HttpResponsePermanentRedirect(redirect_url)
    


type_zodiac = {
        'fire': ['aries', 'leo', 'sagittarius'],
        'earth': ['taurus', 'virgo', 'capricorn'],
        'air': ['gemini', 'libra', 'aquarius'],
        'water': ['cancer', 'scorpio', 'pisces']
    }

zodiac_number = {
        'leo':"♌ Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
        'cancer':"♋ Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
        'aries':"♈ Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
        'taurus':"♉ Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
        'gemini':"♊ Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
        'virgo':"♍ Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
        'libra':"♎ Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
        'scorpio':"♏ Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
        'sagittarius':"♐ Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
        'capricorn':"♑ Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
        'aquarius':"♒ Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
        'pisces':"♓ Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
    }