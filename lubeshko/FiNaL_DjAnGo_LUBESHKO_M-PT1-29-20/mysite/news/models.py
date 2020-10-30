from django.db import models
from django.urls import reverse

# Create your models here.
"""
id-int
title - Varchar
content - Text
created_at -  DataTime
update_at -  DataTime
photo - image
is_pblished - boalean
"""


class News(models.Model):  # Вторичная модель
    title = models.CharField(max_length=150, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Обновление")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    is_pblished = models.BooleanField(default=True, verbose_name="Да/Нет")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                 verbose_name='Категория (!class News)')

    def get_absolute_url(self):
          return reverse("view_news",kwargs={"news_id":self.pk})


    def __str__(self):
        return self.title  # ==//==

    class Meta:
        verbose_name = "Новость (class Meta(models.py)"
        verbose_name_plural = "Новости (class Meta(models.py)"
        ordering = ["created_at"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Имя категории (class Category(models.Model))")

    '''Строим маршруты 2 вариант'''
    def get_absolute_url(self):
          return reverse("category",kwargs={"category_id":self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]
