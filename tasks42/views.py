from django.shortcuts import render
from tasks42.models import Person, RequestObject


def index(request):
    context = {'persons': Person.objects.all()}
    return render(request, "home.html", context)


def requests(request):
    context = {'requests': RequestObject.objects.all()}
    return render(request, "requests.html", context)