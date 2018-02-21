from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.travels),
    url(r'^join/(?P<id>\d+)$', views.join_trip),
    url(r'^add$', views.route_add_plan),
    url(r'^process$', views.create_trip),
    url(r'^destination/(?P<id>\d+)$', views.destination),
]