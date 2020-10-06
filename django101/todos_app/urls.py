from django.urls import path

from todos_app.views import index

urlpatterns = [
    path('', index),
]
