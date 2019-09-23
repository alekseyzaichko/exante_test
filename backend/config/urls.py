from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from apps.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
]