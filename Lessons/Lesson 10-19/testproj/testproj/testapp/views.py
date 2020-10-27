from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post
from testapp.forms import AddPost, AddPostModelForm
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#@permission_required('mytestapp.can_post')
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

def add_post(request):

    if request.method == "POST":

        form = AddPostModelForm(request.POST, request.FILES) #or AddPost

        if form.is_valid():

            post_entry = Post()
            post_entry.author = Author.objects.get(email=request.user.email)
            post_entry.issued = datetime.datetime.now()
            post_entry.title = form.cleaned_data['title']
            post_entry.subtitle = form.cleaned_data['subtitle']
            post_entry.image = form.cleaned_data['image']
            post_entry.post_type = form.cleaned_data['post_type']
            post_entry.content = form.cleaned_data['content']

            post_entry.save()
            return redirect('/mytestapp/')

    form = AddPostModelForm() #or AddPost
    return render(request, 'add_post.html', {'form': form})

def authors(request):
    all_authors = Author.objects.all()
    
    return render(request, 'authors.html', {'authors': all_authors})

class AuthorCreate(CreateView):
    model=Author
    fields='__all__'
    success_url = "/mytestapp/authors/"

class AuthorModify(UpdateView):
    model=Author
    fields=['name']
    success_url = "/mytestapp/authors/"

class AuthorDelete(DeleteView):
    model=Author
    success_url = "/mytestapp/authors/"