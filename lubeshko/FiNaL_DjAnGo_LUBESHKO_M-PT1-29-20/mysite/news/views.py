from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.core.paginator import Paginator

from .forms import News_model  # Из формы
from .forms import UserRegisterForm
from .models import News, Category
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class HomeNews(ListView):
    model = News  # тоже что и news = News.objects.all()
    context_object_name = "news"

    # extra_context = {
    #     'title': 'Главная'
    # }
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная =//='
        return context

    def get_queryset(self):
        return News.objects.filter(is_pblished=True)


class NewsbyCategory(ListView):
    model = News
    context_object_name = "news"
    paginate_by = 2

    # allow_empty = False   #убирает 500 ошибку при пустом списке

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_pblished=True)


""" Можем убрать  "categories": categories, так как создали файл news_tags.py 
def index(request):  # -----------=//=--------------
    # print(dir(request))         # -----------=//=--------------
    news = News.objects.all()
    # categories = Category.objects.all()
    context = {
        "news": news,
        "title": "Список новостей-))-))",
        # "categories": categories,

    }
    return render(request, template_name="news/index.html", context=context)  # -Имя--Вкладки----=//=--
"""
'''
def get_category(request, category_id):  # category_id из <int:category_id> в urls.py
    news = News.objects.filter(category_id=category_id)
    # categories = Category.objects.all() # Можем убрать так как создали файл news_tags.py
    category = Category.objects.get(pk=category_id)
    # return render(request, "news/category.html", {"news": news, "categories": categories, "category": category})
    return render(request, "news/category.html", {"news": news, "category": category})

    """ Можем убрать  "categories": categories, так как создали файл news_tags.py """

'''


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'news/register.html', {'form': form})


def login(request):
    return render(request, 'news/login.html')


def add_news(request):
    if request.method == 'POST':
        form = News_model(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            News.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = News_model()
        cont = {
            "form": form,
        }
    return render(request, template_name="news/add_news.html", context=cont)


def view_news(request, news_id):
    # news_item = News.objects.get(pk = news_id )

    news_item = get_object_or_404(News, pk=news_id)

    return render(request, 'news/view_news.html', {'news_item': news_item})
