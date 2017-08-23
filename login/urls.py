from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.FormView.as_view(), name='login'),
    url(r'^sign/$', views.SignUp.as_view(), name='sign'),
]
