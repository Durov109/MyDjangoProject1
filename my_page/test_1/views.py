from django.shortcuts import render

# Импорт из модели базы данных
from test_1.models import Worker

# Create your views here.


# def index_page(request):
#     all_workers = Worker.objects.all()
#     print(all_workers)


def hello_world(request):
    all_workers = Worker.objects.all()
    print(all_workers)
    return render(request, 'test_index.html')
