from django.conf.urls import url
from musicList import views

urlpatterns = [
    url(r'^create', views.create, name='create'),
    url(r'^list', views.list, name='list'),
]