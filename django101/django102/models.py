from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=30)
    level_of_difficulty = models.IntegerField()
