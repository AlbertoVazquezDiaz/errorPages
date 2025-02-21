from .models import Categoria
from django import forms

class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese nombre de la categoria'
                }
            )
        }

        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la categoria'
        }

        error_messages = {
            'imagen': {
                'required': 'La imagen no puede estar vacio',
                'invalid': 'ingresa un valor valido'
            }
        }