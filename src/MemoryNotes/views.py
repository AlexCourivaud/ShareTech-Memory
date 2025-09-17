from django.shortcuts import render

def index(request):
    return render(request, "MemoryNotes/index.html")

def dashboard(request):
    return render(request, "MemoryNotes/dashboard.html")

def project_index(request):
    return render(request, "MemoryNotes/projects-index.html")

def project_show(request):
    return render(request, "MemoryNotes/project-show.html")

# def project_show

# Pour boucle :
# def article(request, numero_note):
#     if numero_note in ["1", "2", "3"]:
#         return render(request, f"MemoryNotes/project-show_{numero_note}.html")
#     return render(request, "MemoryNotes/notfound.html")