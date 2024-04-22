from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class GamesView(TemplateView):
    template_name = 'game/games.html'

