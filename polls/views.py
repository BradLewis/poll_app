#View file for my first django app
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
