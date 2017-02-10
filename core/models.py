# coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Sport(models.Model):
    name = models.CharField('Nome', max_length=100)
    game_time = models.DecimalField('Tempo do Jogo', max_digits=10, decimal_places=0)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Esporte'
        verbose_name_plural = 'Esportes'


class Game(models.Model):
    name = models.CharField('Nome', max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    score_red = models.DecimalField('Pontos Vermelho', max_digits=10, decimal_places=0)
    score_blue = models.DecimalField('Pontos Azul', max_digits=10, decimal_places=0)
    STATUS_CHOICES = (
        ('Em Andamento', 'Em Andamento'),
        ('Em Breve', 'Em Breve'),
        ('Finalizado', 'Finalizado'),
    )
    status = models.CharField('Status', default='Em Breve', choices=STATUS_CHOICES, max_length=100)
    start = models.DateTimeField('Começa em', null=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
