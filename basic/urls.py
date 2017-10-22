from django.conf.urls import url
from . import views

app_name = 'basic'

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^search/$', views.search, name='query'),
    url(r'^logout/$', views.logOut, name='logout'),
    url(r'^feedback/$', views.feed, name='feed'),
    url(r'^addmusic/$',views.addmusic,name='addmusic'),
    url(r'^addmovie/$',views.addmovie,name='addmovie')
]