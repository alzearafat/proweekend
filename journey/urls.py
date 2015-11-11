from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.journey_list, name='journey_list'),
    url(r'^new/$', views.journey_new, name='journey_new'),
    url(r'^maker/$', views.journey_maker, name='journey_maker'),
    url(r'^detail/(?P<slug>[-\w]+)/$', views.journey_detail, name='journey_detail'),
    url(r'^edit/(?P<slug>[-\w]+)/$', views.journey_edit, name='journey_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)