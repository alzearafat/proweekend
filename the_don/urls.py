from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.about, name='about'),
	url(r'^detail/(?P<pk>[0-9]+)/$', views.team_detail, name='team_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)