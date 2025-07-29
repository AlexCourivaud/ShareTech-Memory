from django.urls import path
from django.contrib import admin

# from django.views.defaults import server_error

from .views import index


urlpatterns = [
    path('admin/', admin.site.urls ),
    path('', index),
]
