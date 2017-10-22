from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('^$', views.dawn, name='dawn'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^basic/', include('basic.urls')),
]
