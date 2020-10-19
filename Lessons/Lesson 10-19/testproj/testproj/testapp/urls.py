from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>', views.post, name='post'),
    path('posts/new/', views.add_post, name='add_post'),
]

urlpatterns += [
    path('authors/', views.authors, name='authors'),
    path('authors/new/', views.AuthorCreate.as_view(), name='author_create'),
    path('authors/<str:pk>/update', views.AuthorModify.as_view(), name='author_modify'),
    path('authors/<str:pk>/delete', views.AuthorDelete.as_view(), name='author_delete'),
]

