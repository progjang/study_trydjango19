from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.posts_home, name='posts_home'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.post_update, name='post_update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.post_delete, name='post_delete'),
]