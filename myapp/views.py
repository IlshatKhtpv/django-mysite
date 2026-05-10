from django.shortcuts import render, redirect, get_object_or_404
from .models import Program, Student, Comment, Page, TaskResult
from django.db.models import Avg, Min, Max, Count
import math

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')


def task(request):
    result = None
    sort = request.GET.get('sort', '-created_at')
    history = TaskResult.objects.all().order_by(sort)

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

        TaskResult.objects.create(
            input_a=A,
            input_h=H,
            input_r=R,
            input_m=M,
            result_text=result
        )



    return render(request, "myapp/task.html", {"result": result, "history": history})


def classmates(request):

    program = Program.objects.first()
    me = Student.objects.filter(role = 'me').first()
    students = Student.objects.filter(role = 'classmate')
    comments = Comment.objects.filter(program=program)

    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        text = request.POST.get('text')
        rating = request.POST.get('rating')

        if nickname and text and rating:
            Comment.objects.create(
                nickname=nickname,
                text=text,
                rating=int(rating),
                program=program
            )
            return redirect('classmates')


    # me = {
    #     "name": "Хатыпов Ильшат Фанилевич",
    #     "photo": "/static/myapp/img/ifkhatypov.jpg",
    #     "email": "ifkhatypov@edu.hse.ru",
    #     "phone": "+7 495 123 45 67"
    # }
    #
    # program = {
    #     "title": "03.03.02 Физика",
    #     "description": "На факультете физики НИУ ВШЭ студенты получают образование мирового уровня в области общей и теоретической физики, а также имеют возможность работать в ведущих научно-исследовательских институтах РАН.",
    #     "supervisor": {
    #         "name": "Трунин Михаил Рюрикович",
    #         "photo": "/static/myapp/img/boss.jpg",
    #         "email": "mtrunin@hse.ru"
    #     },
    #     "manager": {
    #         "name": "Богомазова Вероника Львовна",
    #         "photo": "/static/myapp/img/bog.jpg",
    #         "email": "vbogomazova@hse.ru"
    #     }
    # }
    #
    # students = [
    #     {
    #         "name": "Бузало Мария Григорьевна",
    #         "photo": "/static/myapp/img/mgbuzalo.jpg",
    #         "email": "mgbuzalo@edu.hse.ru",
    #         "phone": "+7 420 228 67 79"
    #     },
    #     {
    #         "name": "Ефремова Мария Александровна",
    #         "photo": "/static/myapp/img/efremova.jpg",
    #         "email": "maalefremova@edu.hse.ru",
    #         "phone": "+7 999 999 99 99"
    #     }
    # ]

    return render(request, "myapp/classmates.html", {
        "me": me,
        "program": program,
        "students": students,
        "comments": comments,
    })


def reviews_list(request):
    reviews = Comment.objects.all()

    # Фильтрация по оценке
    min_rating = request.GET.get('min_rating')
    max_rating = request.GET.get('max_rating')

    if min_rating:
        reviews = reviews.filter(rating__gte=int(min_rating))
    if max_rating:
        reviews = reviews.filter(rating__lte=int(max_rating))

    # Сортировка
    sort = request.GET.get('sort', '-created_date')
    reviews = reviews.order_by(sort)

    # Агрегированная статистика
    stats = Comment.objects.aggregate(
        avg_rating=Avg('rating'),
        min_rating=Min('rating'),
        max_rating=Max('rating'),
        total=Count('id')
    )

    return render(request, 'myapp/reviews_list.html', {
        'reviews': reviews,
        'stats': stats,
    })

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_visible=True)
    return render(request, 'myapp/page_detail.html', {'page': page})
