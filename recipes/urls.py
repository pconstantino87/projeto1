from django.urls import path

from . import views

urlpatterns = [
    path('sobre/', views.sobre),
    path('contato/', views.contato),
    path('', views.home),
    path('recipe/<int:id>/', views.recipe),
]
