from django.contrib import admin

from django102.models.game import Game
from django102.models.person import Person
from django102.models.player import Player


class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ('players',)


admin.site.register(Game, GameAdmin)
admin.site.register(Player)
admin.site.register(Person)
