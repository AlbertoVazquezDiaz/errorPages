from .models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import viewsets, generics #Vamos a crear una vista de varias al mismo tiempo
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from .forms import CustomAlumnCreationForm



class AlumnoViewSet(viewsets.ModelViewSet):
    
    #Permitir saber que objetos se van a mostrar
    queryset = Alumno.objects.all()

    #Permitir saber que serializador se va a usar
    serializer_class = AlumnoSerializer

    #Permitir saber que renderizador se va a usar
    renderer_classes = [JSONRenderer] #Para que nos muestre en formato JSON

    #Establecer los metodos que se van a permitir
    #http_method_names = ['get', 'post']


def formView(request):
    form = CustomAlumnCreationForm()
    return render(request, 'vazquez_alberto.html', {'form': form})