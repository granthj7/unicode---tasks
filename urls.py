from django.urls import path
from . import views

urlpatterns = [
    path('types/', views.pokemon_types, name='pokemon_types'),
    path('select_pokemon_type/', views.select_pokemon_type, name='select_pokemon_type')
]
