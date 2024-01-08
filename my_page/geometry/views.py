from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.


def rectangle(request, width, lenght):
    result = width * lenght
    return HttpResponse(f"Площадь прямоугольника размером {width}x{lenght} равна {result}")


def square(request, width):
    result = width * 2
    return HttpResponse(f"Площадь прямоугольника размером {width}x{width} равна {result}")


def circle(request, radius):
    result = 3.14 * radius**2
    return HttpResponse(f"Площадь круга равна {result}")


def redirect_to_figure(request, **kwargs):
    for i in ('get_rectangle_area', 'get_square_area', 'get_circle_area'):
        if i in request.path:
            return HttpResponsePermanentRedirect(reverse(i.strip('get_'), args=kwargs.values()))