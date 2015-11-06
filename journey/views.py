from django.shortcuts import render, redirect, get_object_or_404
from journey.models import Post
from django.contrib.auth.decorators import login_required
from .forms import JourneyForm
from django.contrib.auth.models import User

def journey_list(request):
	posts = Post.objects.order_by('-tanggal_publish')[:6]
	context = {'posts': posts}
	return render(request, 'journey/journey_list.html', context)

def journey_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'journey/journey_detail.html', {'post': post})

def journey_maker(request):
    if request.user.is_authenticated():
        posts = request.user.user_posts.filter()
        return render(request, 'journey/journey_maker.html', {'posts': posts})
    else:
        return redirect('/journey')

@login_required
def journey_new(request):
    if request.method == "POST":
        form = JourneyForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('journey.views.journey_list')
    else:
        form = JourneyForm()
    return render(request, 'journey/journey_add.html', {'form': form})