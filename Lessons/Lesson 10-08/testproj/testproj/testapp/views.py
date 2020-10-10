from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

def posts(request):
    all_posts = Post.objects.all()
    
    return render(request, 'posts.html', {'posts': all_posts, 'test': 'test'})

def post(request, post_id):
    post = Post.objects.get(id = post_id)
    
    return render(request, 'post.html', {'post': post})
