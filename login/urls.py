from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'login'

urlpatterns = [
    url('^$', views.FormView.as_view(), name='login'),
]
