from rest_framework import generics
from .models import Receta, Categoria, Ingrediente, RecetaIngrediente
from .serializers import RecetaSerializer, CategoriaSerializer, IngredienteSerializer, RecetaIngredienteSerializer


class RecetaListCreate(generics.ListCreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class RecetaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class IngredienteListCreate(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class IngredienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class RecetaIngredienteListCreate(generics.ListCreateAPIView):
    queryset = RecetaIngrediente.objects.all()
    serializer_class = RecetaIngredienteSerializer

class RecetaIngredienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecetaIngrediente.objects.all()
    serializer_class = RecetaIngredienteSerializer
