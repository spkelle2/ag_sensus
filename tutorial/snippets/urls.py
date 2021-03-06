from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# urlpatterns redirect a URL to a specific view 
# (views are what do the work on the objects I made)
urlpatterns = [
        url(r'^snippets/$', views.SnippetList.as_view()),
        url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
        url(r'^users/$', views.UserList.as_view()),
        url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
        ]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
        url(r'^api-auth/', include('rest_framework.urls',
            namespace='rest_framework')),
]
