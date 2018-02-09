from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^session_words$', views.result),
    url(r'^add_word$', views.add_word),
    url(r'^clear$', views.clear_session),
    url(r'^result$', views.result),

]