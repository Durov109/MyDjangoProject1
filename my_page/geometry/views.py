from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


def get_rectangle_area(request, width, lenght):
    result = width * lenght
    return HttpResponse(f"Площадь прямоугольника размером {width}x{lenght} равна {result}")


def get_square_area(request, width):
    result = width * 2
    return HttpResponse(f"Площадь прямоугольника размером {width}x{width} равна {result}")


def get_circle_area(request, radius):
    result = 3.14 * radius**2
    return HttpResponse(f"Площадь круга равна {result}")


def redirect_to_figure(request, **kwargs):
    path = request.path
    figure = path.split('/')[2]
    match figure:
        case 'get_rectangle_area':
            return HttpResponseRedirect(f"/calculate_geometry/rectangle/{kwargs['width']}/{kwargs['lenght']}")
        case 'get_square_area':
            return HttpResponseRedirect(f"/calculate_geometry/square/{kwargs['width']}")
        case 'get_circle_area':
            return HttpResponseRedirect(f"/calculate_geometry/circle/{kwargs['radius']}")
