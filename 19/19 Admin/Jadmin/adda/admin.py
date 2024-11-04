from django.contrib import admin
from .models import Category, News, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # поля для отображения в списке
    search_fields = ('name',) # поле для поиска

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_at','is_published')
    list_filter = ('category','is_published') # список полей для фильтрации
    search_fields = ('title','content')
    list_per_page = 10 # количество новостей на странице

    fieldsets = (     # разбивка полей на секции
        (None, {
            'fields': ('title', 'content', 'category')
        }),
        ('Дополнительные настройки', {  # скрытие секций по умолчанию
'classes': ('collapse',),'fields': ('is_published', 'created_at', 'updated_at')
        }),
    )

    # поля только для чтения
    readonly_fields = ('created_at', 'updated_at')

#   python manage.py runserver