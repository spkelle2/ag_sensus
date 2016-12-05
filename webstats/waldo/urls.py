from django.conf.urls import url

from . import views

app_name = 'waldo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^validate/$', views.validate, name='validate'),
    url(r'^game/$', views.game, name='game'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]

