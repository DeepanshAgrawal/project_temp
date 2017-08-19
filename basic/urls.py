from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'basic'

urlpatterns = [
    url(r'^$', views.Main.as_view() , name= 'index'),
]
