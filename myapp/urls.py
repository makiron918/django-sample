from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^welcome/$', views.welcome, name='welcome'),
  url(r'^like/$', views.like, name='like'),
  url(r'^dislike/$', views.dislike, name='dislike'),
  url(r'^birthday/$', views.birthday, name='birthday'),
]