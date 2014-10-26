from django.shortcuts import render
from tasks42.models import Person, RequestStr


def index(request):
    context = {'persons': Person.objects.all()}
    return render(request, "home.html", context)

<<<<<<< HEAD

def requests(request):
    context = {'requests': RequestStr.objects.all()[:10]}
    return render(request, "requests.html", context)
=======
>>>>>>> t1_contact
