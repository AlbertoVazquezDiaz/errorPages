from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets #Vamos a crear una vista de varias al mismo tiempo
from rest_framework.renderers import JSONRenderer

class ProductoViewSet(viewsets.ModelViewSet):

    #Permitir saber que objetos se van a mostrar
    queryset = Producto.objects.all()

    #Permitir saber que serializador se va a usar
    serializer_class = ProductoSerializer

    #Permitir saber que renderizador se va a usar
    renderer_classes = [JSONRenderer] #Para que nos muestre en formato JSON

    #Establecer los metodos que se van a permitir
    #http_method_names = ['get', 'post']
    

from django.shortcuts import render
from .forms import ProductoForm

def agregar_producto(request):
    form = ProductoForm()
    return render(request, 'agregar.html', {'form':form})