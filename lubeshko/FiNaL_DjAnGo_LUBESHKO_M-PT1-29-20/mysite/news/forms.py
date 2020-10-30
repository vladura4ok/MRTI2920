from django import forms  # 1. Импортируем новость
from .models import Category  # 2. ЧТо б выбрать категорию в форме- импортировали из модели Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Имя пользователя', help_text="Максимум 50 символов",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=15, label='Пароль', help_text="Максимум 15 символов",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=15, label='Подтверждение пароля:', help_text="Максимум 15 символов",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        """Баг джанго. Для пароля здесь не работает"""
        # widgets = {
        #     'username':forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'})
        #
        # }


'''
Создаем класс, и наследуем от формы (forms.Form - не привязаны к модели News)
Поля для формы свои. Смотри документацию
! В формах есть спец. поля для обработки связей, а для многие ко многим ModelMultipleChoiceField
! Для ModelChoiceField есть параметр QuerySet указываем из какой модели данные (Category)
Создали... Далее рендерим во view def add_news(request)

'''


class News_model(forms.Form):
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }))
    content = forms.CharField(label='Контент', required=False, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 5
        }))
    is_pblished = forms.BooleanField(label='Публиковать', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label="Выберите",
                                      widget=forms.Select(
                                          attrs={
                                              "class": "form-control"
                                          }))
