# coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class GameManager(models.Manager):
    def finalize(self, pk):
        game = self.get(pk=pk)
        game.status = 'Finalizado'
        game.save()
        return game

    def initiate(self, pk):
        game = self.get(pk=pk)
        game.status = 'Em Andamento'
        game.save()
        return game

    def add_scorered(self, pk):
        game = self.get(pk=pk)
        game.score_red = game.score_red + 1
        game.save()
        return game

    def add_scoreblue(self, pk):
        game = self.get(pk=pk)
        game.score_blue = game.score_blue + 1
        game.save()
        return game


class Sport(models.Model):
    name = models.CharField('Nome', max_length=100)
    game_time = models.DecimalField('Tempo do Jogo', max_digits=10, decimal_places=0)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Esporte'
        verbose_name_plural = 'Esportes'

    def get_absolute_url(self):
        return "/esportes/"


class Game(models.Model):
    name = models.CharField('Nome', max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    score_red = models.DecimalField('Pontos Vermelho', max_digits=10, decimal_places=0, default=0, editable=False)
    score_blue = models.DecimalField('Pontos Azul', max_digits=10, decimal_places=0, default=0, editable=False)
    status = models.CharField('Status', default='Em Breve', max_length=100, editable=False)
    start = models.DateTimeField('Começa em', null=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    objects = GameManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

    def get_absolute_url(self):
        return "/jogos/"
