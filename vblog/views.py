from django.shortcuts import render
from vblog.models import Video
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def homepage(request):
	videos = Video.objects.order_by('-pubdate')[:8]
	context = {'videos': videos}
	return render(request, 'vblog/homepage.html', context)

@login_required
def video_list(request):
	videos = Video.objects.order_by('-pubdate')[:12]
	context = {'videos': videos}
	return render(request, 'vblog/video_list.html', context)

def video_detail(request, pk):
	video = get_object_or_404(Video, pk=pk)
	return render(request, 'vblog/video_detail.html', {'video': video})
