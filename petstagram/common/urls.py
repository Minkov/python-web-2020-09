from django.urls import path

from common.views import landing_page, original

urlpatterns = [
    path('', landing_page, name='index'),
    path('original/', original),
]
