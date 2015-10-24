from django.shortcuts import render
from the_don.models import Team
from django.shortcuts import redirect, get_object_or_404

def about(request):
	teams = Team.objects.order_by('-pubdate')[:12]
	context = {'teams': teams}
	return render(request, 'the_don/about.html', context)

def team_detail(request, pk):
	team = get_object_or_404(Team, pk=pk)
	return render(request, 'the_don/about_detail.html', {'team': team})