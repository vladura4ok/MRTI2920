from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

def posts(request):
    all_posts = Post.objects.all()

    posts_markup = ''
    for post in all_posts:
        posts_markup += f"<li><h1>{post.title}</h1> <h3>{post.subtitle}</h3></li>"

    return HttpResponse(f"<ul>{posts_markup}</ul>")

def post(request, post_id):
    return HttpResponse(f"<p>post with id {post_id}</p>")
