from django.shortcuts import render
import math

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')
def task(request):
    result = None
    if request.method == "POST":
        A = float(request.POST.get("A"))
        H = float(request.POST.get("H"))
        R = float(request.POST.get("R"))
        M = float(request.POST.get("M"))
        cube_volume = A ** 3
        cylinder_volume = math.pi * R**2 * H
        if M <= cube_volume and M <= cylinder_volume:
            result = "Жидкость помещается в обе ёмкости."
        elif M <= cube_volume:
            result = "Жидкость помещается только в куб."
        elif M <= cylinder_volume:
            result = "Жидкость помещается только в цилиндр."
        else:
            result = "Жидкость не помещается ни в одну ёмкость."
    return render(request, "myapp/task.html", {"result": result})


def classmates(request):

    me = {
        "name": "Хатыпов Ильшат Фанилевич",
        "photo": "/static/myapp/img/ifkhatypov.jpg",
        "email": "ifkhatypov@edu.hse.ru",
        "phone": "+7 495 123 45 67"
    }

    program = {
        "title": "03.03.02 Физика",
        "description": "На факультете физики НИУ ВШЭ студенты получают образование мирового уровня в области общей и теоретической физики, а также имеют возможность работать в ведущих научно-исследовательских институтах РАН.",
        "supervisor": {
            "name": "Трунин Михаил Рюрикович",
            "photo": "/static/myapp/img/boss.jpg",
            "email": "mtrunin@hse.ru"
        },
        "manager": {
            "name": "Богомазова Вероника Львовна",
            "photo": "/static/myapp/img/bog.jpg",
            "email": "vbogomazova@hse.ru"
        }
    }

    students = [
        {
            "name": "Бузало Мария Григорьевна",
            "photo": "/static/myapp/img/mgbuzalo.jpg",
            "email": "mgbuzalo@edu.hse.ru",
            "phone": "+7 420 228 67 79"
        },
        {
            "name": "Ефремова Мария Александровна",
            "photo": "/static/myapp/img/efremova.jpg",
            "email": "maalefremova@edu.hse.ru",
            "phone": "+7 999 999 99 99"
        }
    ]

    return render(request, "myapp/classmates.html", {
        "me": me,
        "program": program,
        "students": students
    })