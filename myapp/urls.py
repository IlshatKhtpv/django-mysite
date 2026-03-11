# myapp/urls.py

from django.urls import path
from .views import home, task, classmates # Импортируем представления из текущего приложения

# Этот список urlpatterns будет подключен к главному urls.py проекта
urlpatterns = [
    path('', home, name='home'),
    path('task/', task, name='task'),
    path('classmates/', classmates, name='classmates'),
]