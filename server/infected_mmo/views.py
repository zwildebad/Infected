from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from .backend import gameClasses
from .backend import main

# THIS IS THE MODEL IN MVC
game_list = []


# Create your views here.
def index(request):
    return render_to_response('index.html')


def game_login(request):
    for i in range(0, len(game_list)):
        current_game = game_list[i]
        if main.login(current_game):
            return render_to_response('game.html')  # return the current game instance
        else:
            new_game = gameClasses.Game()
            game_list.append(new_game)
            main.login(new_game)
            return render_to_response('game.html')  # return new game instance


def game_logout(request, game):
    if main.logout(game):
        return render_to_response('index.html')


def settings(request):
    return render_to_response('settings.html')
