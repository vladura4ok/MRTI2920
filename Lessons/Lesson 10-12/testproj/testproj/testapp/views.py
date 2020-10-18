from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

def posts(request):
    all_posts = Post.objects.all()

    viewed = request.session.get('viewed', '')
    
    return render(request, 'posts.html', {'posts': all_posts, 'viewed': viewed})

def post(request, post_id):
    try:
        post = Post.objects.get(id = post_id)
    except:
        return HttpResponse(status=404)

    viewed = request.session.get('viewed', '')
    viewed += f" {post_id}"
    request.session['viewed'] = viewed
    
    return render(request, 'post.html', {'post': post})
