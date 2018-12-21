from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup),
    url(r'^login$', views.login),
    url(r'^create$', views.create),
    url(r'^welcome$', views.welcome),
    url(r'^chat$', views.comein),
    url(r'^main$', views.chat),
    url(r'^logout$', views.logout),
    url(r'^addfriend/(?P<id>\d+)$', views.addfriend),
    url(r'^remove/(?P<id>\d+)$', views.removefriend),
    url(r'^friend/(?P<id>\d+)/send$', views.send_message),
    url(r'^message/(?P<id>\d+)/delete$', views.delete_message),
    url(r'^back$', views.back),
    url(r'^update$', views.update),
    url(r'^info/(?P<id>\d+)$', views.info),
]