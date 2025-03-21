import django.forms as forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese precio del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese URL de la imagen'
                }
            )
        }
        labels = {
            'nombre': 'Nombre del producto',
            'descripcion': 'Descripcion del producto',
            'precio': 'Precio del producto',
            'stock': 'Stock del producto',
            'imagen': 'URL de la imagen',
            'categoria': 'Categoria del producto'
        }