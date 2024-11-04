from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.name

    # мета-классы в джанго содержат параметры таблицы
    class Meta:
        verbose_name = "Категория"  # более точное имя поля таблицы . без указания будет присвоено имя атрибута указанное в нем
        verbose_name_plural = "Категории" # то же самое для множественного числа


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


#     python manage.py runserver