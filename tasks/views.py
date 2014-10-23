from django.shortcuts import render
from tasks.models import Person


def index(request):
    context = {'persons': Person.objects.all()}
    return render(request, "home.html", context)
