from django.contrib import admin
from django.urls import path, include

# from django.views.defaults import server_error

from .views import index
from MemoryNotes import memory_index

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('', index, name="index"),
    path('MemoryNotes/', memory_index),
]
