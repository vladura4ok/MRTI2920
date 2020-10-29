from django import template  # 1. Импортируем темплэйт
from news.models import Category   # 2. Импортируем категорию

register = template.Library()  # 3. Чтобы быть допустимой библиотекой тегов, модуль должен содержать переменную уровня
# модуля с именем, register которая является template.Library экземпляром, в котором зарегистрированы все
# теги и фильтры. Итак, в верхней части модуля поместите следующее


@register.simple_tag(name='lala')  # 4.Декоратор имя
def get_categories():
    return Category.objects.all()

# 5.Загрузим в _sidebar.html наш созданный тег путем написания {%load news_tags%}

'''
Можем присвоить имя какое хотим
@register.simple_tag(name=”lala”)  # 4.Декоратор имя
def get_categories():
    return Category.objects.all()
Но тогда _sidebar.html
{% вместо get_categories пишем lala as categories %}

'''

'''
Создадим inclusion tag где в скобках укажем путь к нашему news/list_category.html
Туда из _sidebar.html скопировали сайдбар
А в сайдбаре написали {% show_category %}. Посмотрим что получ.
Еще добавил аргументы
'''

@register.inclusion_tag('news/list_category.html')
def show_category(arg1="inclusion_", arg2="tag"):
    categories = Category.objects.all()
    return {"categories":categories, "arg1":arg1, "arg2":arg2}