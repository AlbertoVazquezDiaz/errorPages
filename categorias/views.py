from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import categoriaForm
import json as Json


def lista_categorias(request):
    categorias = Categoria.objects.all()

    data = [{"nombre": c.nombre, "imagen": c.imagen} for c in categorias]

    return JsonResponse(data, safe=False)


def agregar_categoria(request):
    if request.method == "POST":
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categorias")
    else:
        form = categoriaForm()
    return render(request, "regCategoria.html", {"form": form})


def registrar_categoria(request):
    if request.method == "POST":
        try:
            data = Json.loads(request.body)
            categoria = Categoria.objects.create(
                nombre=data["nombre"], imagen=data["imagen"]
            )
            return JsonResponse(
                {"mensaje": "Categoria registrada correctamente"}, status=200
            )
        except Exception as e:
            return JsonResponse({"mensaje": "Error al registrar categoria"}, status=400)
    return JsonResponse({"mensaje": "Metodo no permitido"}, status=405)


def vista_categorias(request):
    return render(request, "categorias.html")
