from django.conf.urls import url
from collect import views

urlpatterns = [
    url(r'^missions/$', views.mission_list),
]
