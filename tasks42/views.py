from django.shortcuts import render
from tasks42.models import Person


def index(request):
    context = {'persons': Person.objects.all()}
    return render(request, "home.html", context)
