from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    age = models.IntegerField(default=0, blank=False)
