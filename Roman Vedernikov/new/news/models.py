from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Articles(models.Model):
    title = models.CharField('Название', max_length=150)
    anons = models.CharField('Анонс', max_length=4000)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', default=datetime.datetime.now())
    author = models.CharField('Автор', max_length=50)
    image = models.ImageField('Фото', upload_to='./uploads', default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


