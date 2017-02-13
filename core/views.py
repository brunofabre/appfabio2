# coding=utf-8

from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, RedirectView, CreateView, DeleteView
from .models import Game, Sport
from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class GamesView(LoginRequiredMixin, ListView):
    model = Game
    ordering = '-pk'
    context_object_name = 'games'
    template_name = 'pages/games.html'


class CreateGameView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Game
    permission_required = 'core'
    fields = ['name', 'sport', 'start']
    template_name = 'pages/creategame.html'


class SportsView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Sport
    permission_required = 'core'
    context_object_name = 'sports'
    template_name = 'pages/sports.html'


class CreateSportView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Sport
    permission_required = 'core'
    fields = ['name', 'game_time']
    template_name = 'pages/createsport.html'


class SportDeleteView(LoginRequiredMixin, DeleteView):
    model = Sport
    success_url = reverse_lazy('core:sports')


class FinalizeView(PermissionRequiredMixin, LoginRequiredMixin, RedirectView):
    permission_required = 'core'
    def get_redirect_url(self, *args, **kwargs):
        finalized = Game.objects.finalize(self.kwargs['pk'])
        return reverse_lazy('core:games')


class InitiateView(PermissionRequiredMixin, LoginRequiredMixin, RedirectView):
    permission_required = 'core'
    def get_redirect_url(self, *args, **kwargs):
        initiated = Game.objects.initiate(self.kwargs['pk'])
        return reverse_lazy('core:games')


class AddScoreRedView(PermissionRequiredMixin, LoginRequiredMixin, RedirectView):
    permission_required = 'core'
    def get_redirect_url(self, *args, **kwargs):
        scored_red = Game.objects.add_scorered(self.kwargs['pk'])
        return reverse_lazy('core:games')


class AddScoreBlueView(PermissionRequiredMixin, LoginRequiredMixin, RedirectView):
    permission_required = 'core'
    def get_redirect_url(self, *args, **kwargs):
        scored_blue = Game.objects.add_scoreblue(self.kwargs['pk'])
        return reverse_lazy('core:games')


home = HomeView.as_view()
games = GamesView.as_view()
creategame = CreateGameView.as_view()
sports = SportsView.as_view()
createsport = CreateSportView.as_view()
sportdelete = SportDeleteView.as_view()

finalize = FinalizeView.as_view()
initiate = InitiateView.as_view()
add_score_red = AddScoreRedView.as_view()
add_score_blue = AddScoreBlueView.as_view()
