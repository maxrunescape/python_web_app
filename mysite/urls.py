from django.conf.urls import include, url
from django.contrib import admin

import snippets

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^polls_api/', include('polls_api.urls')),
    url(r'^snippets/', include('snippets.urls')),
    url(r'^users/$', snippets.views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', snippets.views.UserDetail.as_view()),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]