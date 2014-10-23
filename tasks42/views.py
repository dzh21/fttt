from django.shortcuts import render
from tasks42.models import Person, RequestStr


def index(request):
    context = {'persons': Person.objects.all()}
    return render(request, "home.html", context)


def requests(request):
    context = {'requests': RequestStr.objects.all()[:10]}
    return render(request, "requests.html", context)