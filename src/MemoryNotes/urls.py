from django.urls import path
from .views import index, dashboard, project_show, project_index

# from django.views.defaults import server_error



urlpatterns = [
    path('', index, name="MemoryNotes-index"),
    path('dashboard/', dashboard, name="memory-dashboard"),
    path('project_index/', project_index, name="memory-project-index"),
    path('project_show/', project_show, name="memory-index"),
    
]
# notes : pour boucle : note-xx
# path('note-<int:numero_note>/', note, name="memory-note")