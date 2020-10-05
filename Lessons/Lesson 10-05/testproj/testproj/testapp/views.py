from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

def posts(request):
    all_posts = Post.objects.all()
    
    return render(request, 'posts.html', {'posts': all_posts, 'test': 'test'})

def post(request, post_id):
    return HttpResponse(f"<p>post with id {post_id}</p>")
