from django.urls import path  # -----------=//=--------------
from .views import *  # -----------=//=--------------

urlpatterns = [
    path('register/', register, name ='register'),
    path('login/', login, name ='login'),
    # path("", index, name="home"),  # -----------=//=--------------
    path('', HomeNews.as_view(), name="home"),  # ListView
    # path("test/", test),
    # path('cat/<int:category_id>/', get_category, name='category'),
    path('cat/<int:category_id>/', NewsbyCategory.as_view(extra_context={'title':'Категория!'}), name='category'),
    path('news/add-news/', add_news, name="add_news"),
    path('news/<int:news_id>', view_news, name='view_news'),
]
