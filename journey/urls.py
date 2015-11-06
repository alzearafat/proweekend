from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.journey_list, name='journey_list'),
    url(r'^new/$', views.journey_new, name='journey_new'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.journey_detail, name='journey_detail'),
    url(r'^maker/$', views.journey_maker, name='journey_maker'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)