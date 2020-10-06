from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.views.generic import ListView

from django102.models.game import Game


def something(request):
    return HttpResponse("<u>It works!</u>")


def index(request):
    title = 'SoftUni Django 101'
    users = User.objects.all()
    games = Game.objects.all_with_players_count()

    context = {
        'title': title,
        'users': users,
        'games': games,
        # 'users': [],
    }

    print(users.query)

    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class view'
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'


@require_GET
def methods_demo(request):
    context = {
        'name': 'Doncho',
        'age': 19,
    }

    if request.content_type == 'application/json':
        return JsonResponse(context)

    return render(request, 'methods_demo.html', context)


def raises_exception(request):
    raise Exception('Raises')


def create_game(request):
    game = Game(
        name='LoL',
        level_of_difficulty=Game.EASY,
    )
    game.save()
    return redirect(request, 'index')
