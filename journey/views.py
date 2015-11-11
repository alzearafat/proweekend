from django.shortcuts import render, redirect, get_object_or_404
from journey.models import Post
from django.contrib.auth.decorators import login_required
from .forms import JourneyForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

def journey_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'journey/journey_list.html', {"posts": posts})

def journey_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'journey/journey_detail.html', {'post': post})

def journey_maker(request):
    if request.user.is_authenticated():
        posts = request.user.user_posts.filter()
        paginator = Paginator(posts, 6)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'journey/journey_maker.html', {'posts': posts})
    else:
        return redirect('/accounts/login')

@login_required
def journey_new(request):
    if request.method == "POST":
        form = JourneyForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.tanggal_publish = datetime.datetime.now()
            post.save()
            return redirect('journey.views.journey_list')
    else:
        form = JourneyForm()
    return render(request, 'journey/journey_add.html', {'form': form})

@login_required
def journey_edit(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = JourneyForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.tanggal_publish = datetime.datetime.now()
            post.save()
            return redirect('journey.views.journey_detail', slug=slug)
    elif not request.user == post.author:
        return redirect('/journey')
    else:
        form = JourneyForm(instance=post)
    return render(request, 'journey/journey_edit.html', {'form': form})