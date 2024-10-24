Requisitos
Python 3.7+
Django 5.1+
Django REST Framework
Instalación
Clona el repositorio:

bash
Copiar código
git clone https://github.com/tu_usuario/api-recetas-ingredientes.git
cd api-recetas-ingredientes
Crea y activa un entorno virtual (opcional pero recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Aplica las migraciones de la base de datos:

bash
Copiar código
python manage.py migrate
Inicia el servidor:

bash
Copiar código
python manage.py runserver
Endpoints de la API
Listar y Crear Recetas
URL: /api/recetas/

Métodos: GET, POST

GET: Retorna la lista de todas las recetas.
POST: Crea una nueva receta.
Ejemplo de datos para POST:

json
Copiar código
{
    "nombre": "Tarta de Manzana",
    "descripcion": "Una receta clásica de tarta de manzana.",
    "categoria_id": 1
}
Detalle, Actualizar y Eliminar Recetas
URL: /api/recetas/<id>/
Métodos: GET, PUT, PATCH, DELETE
Listar y Crear Ingredientes
URL: /api/ingredientes/
Métodos: GET, POST
Detalle, Actualizar y Eliminar Ingredientes
URL: /api/ingredientes/<id>/
Métodos: GET, PUT, PATCH, DELETE
Listar y Crear Categorías
URL: /api/categorias/
Métodos: GET, POST
Detalle, Actualizar y Eliminar Categorías
URL: /api/categorias/<id>/
Métodos: GET, PUT, PATCH, DELETE
Modelos
El proyecto está compuesto por los siguientes modelos:

Receta

id: clave primaria.
nombre: nombre de la receta.
descripcion: descripción de la receta.
categoria: relación con la tabla Categoría.
Ingrediente

id: clave primaria.
nombre: nombre del ingrediente.
cantidad: cantidad del ingrediente.
unidad: unidad de medida del ingrediente.
Categoría

id: clave primaria.
nombre: nombre de la categoría.
RecetaIngrediente

id: clave primaria.
receta: relación con la tabla Receta.
ingrediente: relación con la tabla Ingrediente.
Validaciones
Se han implementado validaciones en los serializadores de los modelos para asegurar la integridad de los datos ingresados.

Ejemplo de Validaciones
Validación del campo cantidad en el modelo Ingrediente, que se asegura de que sea un número positivo.

python
Copiar código
def validate_cantidad(self, value):
    if not value.isdigit() or int(value) <= 0:
        raise serializers.ValidationError("La cantidad debe ser un número positivo.")
    return value
Validación del campo unidad, que se asegura de que sea una unidad de medida válida.

python
Copiar código
UNIDADES_VALIDAS = ['gramos', 'mililitros', 'piezas']

def validate_unidad(self, value):
    if value not in UNIDADES_VALIDAS:
        raise serializers.ValidationError(f"Unidad no válida. Debe ser una de {', '.join(UNIDADES_VALIDAS)}.")
    return value
Rutas
El archivo de rutas define las URL para interactuar con los endpoints de la API:

python
Copiar código
from django.urls import path
from . import views

urlpatterns = [
    path('recetas/', views.RecetaListCreate.as_view(), name='receta-list'),
    path('recetas/<int:pk>/', views.RecetaDetail.as_view(), name='receta-detail'),
    path('ingredientes/', views.IngredienteListCreate.as_view(), name='ingrediente-list'),
    path('ingredientes/<int:pk>/', views.IngredienteDetail.as_view(), name='ingrediente-detail'),
    path('categorias/', views.CategoriaListCreate.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
]
Ejecutar Pruebas
Para ejecutar las pruebas unitarias, usa el siguiente comando:

bash
Copiar código
python manage.py test
Tecnologías Usadas
Django: Framework web de alto nivel.
Django REST Framework: Extensión para construir APIs RESTful.
SQLite: Base de datos por defecto del proyecto.
Contribuir
Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Haz commit de tus cambios (git commit -m 'Agrega nueva funcionalidad').
Empuja la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.