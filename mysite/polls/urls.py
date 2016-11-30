from django.conf.urls import url

# from current directory import views
from . import views # import from the current package/directory

app_name = 'polls'
urlpatterns = [
    # example: /polls/
    url(r'^$', views.index, name='index'),

    # example: /polls/2/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # example: /polls/2/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # example: /polls/2/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
