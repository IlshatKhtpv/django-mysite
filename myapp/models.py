from django.db import models
from django.utils import timezone # Для установки времени по умолчанию



# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название программы")
    description = models.TextField(verbose_name="Описание программы")

    supervisor_name = models.CharField(max_length=100, verbose_name="Декан (ФИО)")
    supervisor_photo = models.ImageField(upload_to='staff/', verbose_name="Фото декана")
    supervisor_email = models.EmailField(verbose_name="Email декана")

    manager_name = models.CharField(max_length=100, verbose_name="Менеджер (ФИО)")
    manager_photo = models.ImageField(upload_to='staff/', verbose_name="Фото менеджера")
    manager_email = models.EmailField(verbose_name="Email менеджера")

    class Meta:
        verbose_name = 'Образовательная программа'
        verbose_name_plural = "Образовательные программы"


    def __str__(self):
        return self.title

class Student(models.Model):
    ROLE_CHOICES = [('me', 'Я'), ('classmate', 'Однокурсник'),]

    name = models.CharField(max_length=100, verbose_name="ФИО")
    photo = models.ImageField(upload_to='students/', verbose_name="Фото")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    role = models.CharField(choices=ROLE_CHOICES, default = 'classmate', max_length=100)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = "Студенты"
    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"

class Comment(models.Model):
    nickname = models.CharField(max_length=200, verbose_name="Ник")
    text = models.TextField(verbose_name="Текст отзыва")
    created_date = models.DateTimeField(default=timezone.now)
    rating = models.PositiveSmallIntegerField(verbose_name="Оценка")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='reviews', verbose_name="Образовательная программа")
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_date']

    def __str__(self):
        return f"Отзыв от {self.nickname} ({self.rating}/10)"

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-адрес")
    content = models.TextField(verbose_name="Содержание")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок в навигации")
    is_visible = models.BooleanField(default=True, verbose_name="Отображать в навигации")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class TaskResult(models.Model):
    input_a = models.FloatField(verbose_name="Ребро куба A")
    input_h = models.FloatField(verbose_name="Высота H")
    input_r = models.FloatField(verbose_name="Радиус R")
    input_m = models.FloatField(verbose_name="Объём M")
    result_text = models.CharField(max_length=200, verbose_name="Результат")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Результат задачи"
        verbose_name_plural = "Результаты задачи"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.result_text} ({self.created_at:%d.%m.%Y %H:%M})"