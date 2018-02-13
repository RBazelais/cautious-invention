from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.users.urls')),
    # url(r'^blogs/', include('apps.blogs.urls')),
    # url(r'^surveys/', include('apps.surveys.urls'))
]
