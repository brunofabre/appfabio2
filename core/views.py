# coding=utf-8

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Game


class HomeView(generic.TemplateView):
    template_name = 'pages/home.html'


class GamesView(LoginRequiredMixin, generic.ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'pages/games.html'


home = HomeView.as_view()
games = GamesView.as_view()
