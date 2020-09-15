from django.contrib import admin
from django.urls import path

from django101.views import index, UsersListView, GamesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
]
