from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
    url(r'^videos/$', views.video_list, name='video_list'),
    url(r'^videos/detail/(?P<pk>[0-9]+)/$', views.video_detail, name='video_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)