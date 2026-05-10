# myapp/urls.py

from django.urls import path
from .views import home, task, classmates, reviews_list, page_detail # Импортируем представления из текущего приложения

# Этот список urlpatterns будет подключен к главному urls.py проекта
urlpatterns = [
    path('', home, name='home'),
    path('task/', task, name='task'),
    path('classmates/', classmates, name='classmates'),
    path('reviews_list/', reviews_list, name='reviews'),
    path('page/<slug:slug>/', page_detail, name='page_detail'),

]