from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('102/', include('django102.urls')),
    path('admin/', admin.site.urls),
    path('', include('django102.urls')),
    path('todos/', include('todos_app.urls')),
]
