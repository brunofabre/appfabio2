# coding=utf-8

from django.views import generic

class HomeView(generic.TemplateView):
    template_name = 'pages/home.html'



home = HomeView.as_view()