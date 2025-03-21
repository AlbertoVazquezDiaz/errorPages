from django import forms
from .models import Alumno

class CustomAlumnCreationForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["id", "nombre", "apellido", "edad", "matricula", "correo"]
        widgets = {
            'id': forms.HiddenInput(),  
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }
