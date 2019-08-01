from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Market, Scrap
from .forms import PostForm


# Create your views here.

def store(request):
    #이화가 구현한 시간순 정렬.. 크으
    posts = Market.objects.order_by('-pub_date')
    return render(request, 'store.html', {'posts': posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Market, pk = post_id)
    scrap_count = 3
    
    if request.user.is_authenticated():
        scrap = Scrap.objects.filter(user=request.user, post=post_detail)
        return render(request, 'detail.html', {'post': post_detail, 'scrap':scrap, 'count':scrap_count})
    else :
        return render(request, 'detail.html', {'post': post_detail, 'count':scrap_count})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user.get_username())
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
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, post_id):
    post = get_object_or_404(Market, pk=post_id)
    post.delete()
    return redirect('store')

def scrap(request, post_id):
    post = get_object_or_404(Market, pk=post_id)
    scrapped = Scrap.objects.filter(user=request.user, post=post)
    if not scrapped:
        Scrap.objects.create(user=request.user, post=post)
    #request.user는 현재 로그인한 user
    else:
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



#서치기능
def result(request):
    post_object = Market.objects
    query = request.GET.get('query','')
    if query:
        post_object = post_object.filter(title__contains=query).order_by('-pub_date')
        return render(request, 'result.html', {'result':post_object})