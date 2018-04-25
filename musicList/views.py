from django.shortcuts import render_to_response,render, redirect
from musicList.models import Post
from musicList.forms import PostForm


# Create your views here.
def list(request):
    full_list = Post.objects.all()
    return render_to_response('musicList/indexlist.html', {'full_list': full_list})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/musicList/list')
    else:
        form = PostForm()

    return render(request, 'musicList/index.html', {'form': form})