from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^polls_api/', include('polls_api.urls')),
    url(r'^api/', include('snippets.urls')),
]