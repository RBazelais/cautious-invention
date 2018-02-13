from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blogs$', views.index),
    url(r'^blogs/new$', views.new),
    url(r'^blogs/create$', views.create),
    url(r'^blogs/(?<id>\d+)$', views.show),
    url(r'^blogs/(?<id>\d+)/edit$', views.edit),
    url(r'^blogs/(?<id>\d+)/delete$', views.delete),

]