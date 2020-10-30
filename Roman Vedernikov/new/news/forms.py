from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ImageField, FileInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            # "date": DateTimeInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Дата статьи'
            # }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "image": FileInput(attrs={
                    'placeholder': 'Фото'
            }),
        }


# class UserCreationForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
#
#         widgets = {
#             "title": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Название Статьи'
#             }),
#             "anons": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Анонс статьи'
#             }),
#             # "date": DateTimeInput(attrs={
#             #     'class': 'form-control',
#             #     'placeholder': 'Дата статьи'
#             # }),
#             "full_text": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Текст статьи'
#             }),
#             "image": FileInput(attrs={
#                     'placeholder': 'Фото'
#             }),
#         }