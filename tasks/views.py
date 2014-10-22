from django.shortcuts import render
from tasks.models import Person


def index(request):
    context = {'person': Person.objects.all()[0]}
    return render(request, "home.html", context)
