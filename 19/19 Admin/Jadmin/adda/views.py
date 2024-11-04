
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import News
from django.db import models



def post_list(request):
    # получаем все посты
    posts = News.objects.all()
    per_page = request.GET.get('per_page', 3) # количество постов
    paginator = Paginator(posts, per_page)
    page_number = request.GET.get('page')  # получаем номер страницы, на которую переходит пользователь
    page_obj = paginator.get_page(page_number)  # получаем посты для текущей страницы
    context = {'page_obj': page_obj, 'per_page': per_page,} # передаем контекст в шаблон

    return render(request, 'index.html', context)



#     python manage.py runserver