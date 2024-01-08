from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:lenght>', views.rectangle, name='rectangle_area'),
    path('square/<int:width>', views.square, name='square_area'),
    path('circle/<int:radius>', views.circle, name='circle_area'),

    path('get_rectangle_area/<int:width>/<int:lenght>', views.redirect_to_figure),
    path('get_square_area/<int:width>', views.redirect_to_figure),
    path('get_circle_area/<int:radius>', views.redirect_to_figure),
]
