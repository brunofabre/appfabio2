# coding=utf-8

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^jogos/', include('games.urls', namespace='games')),

    url(r'^entrar/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': '/'}, name='logout'),
]
