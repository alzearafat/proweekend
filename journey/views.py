from django.shortcuts import render, redirect, get_object_or_404
from journey.models import Post
from django.contrib.auth.decorators import login_required
from .forms import JourneyForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def journey_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6) # Show 25 post per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'journey/journey_list.html', {"posts": posts})


def journey_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'journey/journey_detail.html', {'post': post})

def journey_maker(request):
    if request.user.is_authenticated():
        posts = request.user.user_posts.filter()
        return render(request, 'journey/journey_maker.html', {'posts': posts})
    else:
        return redirect('/accounts/login')

@login_required
def journey_new(request):
    if request.method == "POST":
        form = JourneyForm(request.POST, request.FILES)
        if form.is_valid():
            post.author = request.user
            post = form.save()
            post.save()
            return redirect('journey.views.journey_list')
    else:
        form = JourneyForm()
    return render(request, 'journey/journey_add.html', {'form': form})

@login_required
def journey_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = JourneyForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('journey.views.journey_detail', pk=post.pk)
    elif not request.user == post.author:
        return redirect('/journey')
    else:
        form = JourneyForm(instance=post)
    return render(request, 'journey/journey_edit.html', {'form': form})