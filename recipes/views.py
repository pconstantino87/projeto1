from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# HTTP REQUEST <- HTTP RESPONSE


def home(request):
    return render(request, 'recipes/home.html', {'name': 'Pedro Tiago'})


def sobre(request):
    return HttpResponse('UMA LINDA sobre')


def contato(request):
    return HttpResponse('CONTATO')