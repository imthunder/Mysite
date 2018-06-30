from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    url(r'^(?P<pid>\d+)/$', views.list_view, name='list'),
    url(r'^(?P<pid>\d+)/(?P<detail_id>\d+)$', views.detail_view, name='detail'),
]
