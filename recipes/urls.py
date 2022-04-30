from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('sobre/', sobre),
    path('contato/', contato),
    path('', home),
    path('home', home)
]
