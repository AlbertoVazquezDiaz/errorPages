from django.urls import path
from .views import *


urlpatterns = [
    path("api/get/", lista_categorias, name="lista"),
    path("registrar/", agregar_categoria, name="registrar"),
    path("json/", vista_categorias, name="categorias"),
    path("api/post/", registrar_categoria, name="registrar_categoria"),
]
