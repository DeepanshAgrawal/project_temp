from django.conf.urls import url
from . import views

app_name = 'basic'

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^search/$', views.search, name='query'),
    url(r'^logout/$', views.logOut, name='logout'),
    url(r'^feedback/$', views.feed, name='feed'),
    url(r'^addmusic/$',views.addobject,name='addmusic'),
    url(r'^addmovie/$',views.addobject,name='addmovie'),
    url(r'^message/$', views.addobject, name='message'),
    url(r'^inbox/$', views.inbox, name='inbox'),
]