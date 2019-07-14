from django.shortcuts import render, get_object_or_404, redirect
from .models import Market
from .forms import PostForm


# Create your views here.

def store(request):
    posts = Market.objects
    return render(request, 'store.html', {'posts': posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Market, pk = post_id)
    return render(request, 'detail.html', {'post': post_detail})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('store')
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})

def edit(request):
    return render(request, 'edit.html')

def postupdate(request, post_id):
    post = get_object_or_404(Market, pk = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, post_id):
    post = get_object_or_404(Market, pk=post_id)
    post.delete()
    return redirect('store')