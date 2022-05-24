from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('sobre/', views.sobre),
    path('contato/', views.contato),
    path('', views.home, name="home"),
    path('recipe/category/<int:category_id>/', views.category, name="category"),
    path('recipe/<int:id>/', views.recipe, name="recipes-recipe"),

]
