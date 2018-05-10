from django.shortcuts import render_to_response,render, redirect, HttpResponse
from django.contrib.auth.models import User
from musicList.models import Post
from musicList.forms import PostForm


def list(request):
    contents = Post.objects.all()
    return render_to_response('musicList/indexlist.html', {'contents': contents})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/musicList/list')
    else:
        form = PostForm()

    return render(request, 'musicList/index.html', {'form': form})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username = username,
            email = email,
            password = password,
        )
        return list(request)

    else:
        return render(request, 'musicList/regist.html')