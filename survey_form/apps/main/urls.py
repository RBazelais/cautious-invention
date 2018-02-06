from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset$', views.reset),
    url(r'^surveys/process$', views.process),
    url(r'^result$', views.result),
    url(r'^go_back$', views.go_back),
]