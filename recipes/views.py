import django
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe

#from utils.recipes.factory import make_recipe


# Create your views here.

# HTTP REQUEST <- HTTP RESPONSE


def home(request):
    #recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')
    recipes = get_list_or_404(Recipe, is_published=True)
    return render(request, 'recipes/home.html', context={"recipes": recipes, "page_title": 'Home'})


def recipe(request, id):
    #recipe = Recipe.objects.filter(pk=id, is_published=True).first()
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    return render(request, 'recipes/page/recipe-view.html', context={'recipe': recipe, 'is_detail_page': True, "page_title": 'Receitas'})


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id, is_published=True).order_by('-id')

    # if not recipes:
    # COMO RETORNA UM 404 FORMA 1
    # return HttpResponse('Not found', status=404)
    #
    # RETORNADO UM 404 FORMA 2
    # raise Http404('Não achamos')
    # TERCEIRA FORMA DE RECUPERAR DADOS OU 404
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id'))

    return render(request, 'recipes/home.html', context={
        'recipes': recipes,
        'page_title': 'Categoria',
        'category_name': f'{recipes[0].category.name}',
    })


def sobre(request):
    return HttpResponse('UMA LINDA sobre')


def contato(request):
    return HttpResponse('CONTATO')
