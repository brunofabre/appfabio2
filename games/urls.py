# coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.games, name='home'),
    url(r'^adicionar/$', views.creategame, name='creategame'),
    url(r'^esportes/$', views.sports, name='sports'),
    url(r'^esportes/adicionar/$', views.createsport, name='createsport'),
    url(r'^esportes/(?P<pk>[\d]+)/delete/$', views.sportdelete, name='deletesport'),

    url(r'^finalizar/(?P<pk>[\d]+)/$', views.finalize, name='finalize'),
    url(r'^iniciar/(?P<pk>[\d]+)/$', views.initiate, name='initiate'),

    url(r'^add-scorered/(?P<pk>[\d]+)/$', views.add_score_red, name='add_score_red'),
    url(r'^add-scoreblue/(?P<pk>[\d]+)/$', views.add_score_blue, name='add_score_blue'),
]