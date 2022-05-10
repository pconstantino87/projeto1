from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.

# HTTP REQUEST <- HTTP RESPONSE


def home(request):
    return render(request, 'recipes/home.html', context={"recipes": [make_recipe()for _ in range(11)]})


def recipe(request, id=False):
    return render(request, 'recipes/page/recipe-view.html', context={'recipe': make_recipe(), 'is_detail_page': True, })


def sobre(request):
    return HttpResponse('UMA LINDA sobre')


def contato(request):
    return HttpResponse('CONTATO')
