from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
# Create your views here.


def addPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addPost')
    else:
        form = PostForm()
    return render(request, 'addPost.html', {'data': form})


def editPost(request,id):
    post=Post.objects.get(pk=id)
    form = PostForm(instance=post)
    print(post.title)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'addPost.html', {'data': form})


def deletePost(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')