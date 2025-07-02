from django.http import HttpResponse


def vue_de_test(resquest):
    return HttpResponse("<h1> Vue de Test </h1>")