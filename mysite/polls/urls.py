from django.conf.urls import url

from . import views # import from the current package/directory

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
