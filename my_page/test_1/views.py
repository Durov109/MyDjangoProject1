from django.shortcuts import render

# Импорт из модели базы данных
from test_1.models import Worker

# Create your views here.


def primery(request):
    # Вывести все данные из таблицы
    all_workers = Worker.objects.all()
    print(all_workers)

    # Фильтр по зарплате
    worker_filtered_salary = Worker.objects.filter(salary=60000)
    print(worker_filtered_salary)

    # Запись в БД
    new_worker = Worker(name='Иван', surmane='Иванов', salary=70000)
    new_worker.save()
    # или
    Worker.objects.create(name='Иван', surmane='Иванов', salary=70000)

    # Изменение уже существующей записи
    worker_to_change = Worker.object.get(id=1)
    worker_to_change.surname = 'Суворов'
    worker_to_change.save()
    # или
    Worker.objects.filter(id=1).update(name='Суворов')

    # Удаление записи
    Worker.objects.get(id=1).delete()


def hello_world(request):
    return render(request, 'test_index.html', context={'data': 5})


def views_all_worker(request):
    all_workers = Worker.objects.all()
    return render(request, 'views_all_worker.html', {'data': all_workers})
