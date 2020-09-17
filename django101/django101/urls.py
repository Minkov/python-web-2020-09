from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('102/', include('django102.urls')),
    path('', include('django102.urls')),
]
