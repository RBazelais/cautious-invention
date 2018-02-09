from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset$', views.reset),
    url(r'^amadon/buy$', views.process),
    url(r'^checkout$', views.checkout),
    url(r'^go_back$', views.go_back),
]