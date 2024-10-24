from django.urls import path
from . import views

urlpatterns = [

    path('recetas/', views.RecetaListCreate.as_view(), name='receta-list'),
    path('recetas/<int:pk>/', views.RecetaDetail.as_view(), name='receta-detail'),

    path('categorias/', views.CategoriaListCreate.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),

    path('ingredientes/', views.IngredienteListCreate.as_view(), name='ingrediente-list'),
    path('ingredientes/<int:pk>/', views.IngredienteDetail.as_view(), name='ingrediente-detail'),

    path('receta-ingredientes/', views.RecetaIngredienteListCreate.as_view(), name='receta-ingrediente-list'),
    path('receta-ingredientes/<int:pk>/', views.RecetaIngredienteDetail.as_view(), name='receta-ingrediente-detail'),
]
