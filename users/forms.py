import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "name",
            "surname",
            "control_number",
            "age",
            "tel",
            "password1",
            "password2",
        ]

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Correo electrónico",
                    "pattern": "^[a-zA-Z0-9._%+-]+@utez\\.edu\\.mx$",
                    "title": "El correo debe pertenecer al dominio @utez.edu.mx",
                    "required": "required",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre",
                    "minlength": "2",
                    "maxlength": "50",
                    "title": "El nombre debe tener entre 2 y 50 caracteres",
                    "required": "required",
                }
            ),
            "surname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Apellidos",
                    "minlength": "2",
                    "maxlength": "50",
                    "title": "El apellido debe tener entre 2 y 50 caracteres",
                    "required": "required",
                }
            ),
            "control_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Matrícula",
                    "pattern": "^[0-9A-Za-z]{10}$",
                    "title": "La matrícula debe ser alfanumerica y de 10 dígitos.",
                    "required": "required",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Edad",
                    "min": "18",
                    "max": "99",
                    "title": "Debes ser mayor de 18 años",
                    "required": "required",
                }
            ),
            "tel": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Teléfono",
                    "pattern": "^[0-9]{10}$",
                    "title": "El teléfono debe contener exactamente 10 dígitos numéricos.",
                    "required": "required",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contraseña",
                    "pattern": "^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$",
                    "title": "Debe tener al menos 8 caracteres, incluir una mayúscula, un número y un símbolo (!, #, $, %, & o ?)",
                    "required": "required",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Confirmar contraseña",
                    "pattern": "^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$",
                    "title": "Debe coincidir con la contraseña y seguir el mismo formato",
                    "required": "required",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$", email):
            raise forms.ValidationError("El correo debe pertenecer al dominio @utez.edu.mx")
        return email
    
    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        print("Antes del if")
        if not re.match(r"^[0-9]{5}[A-Za-z]{2}[0-9]{3}$", control_number):
            print("Dentro del if")
            raise forms.ValidationError("La matrícula debe ser alfanumerica y de 10 dígitos.")
        return control_number

    
    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        if not re.match(r"^[0-9]{10}$", tel):
            raise forms.ValidationError("El teléfono debe contener exactamente 10 dígitos numéricos.")
        return tel
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not re.match(r"^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$", password1):
            raise forms.ValidationError("Debe tener al menos 8 caracteres, incluir una mayúscula, un número y un símbolo (!, #, $, %, & o ?)")
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
    
    
    
    

    
    
   
    


class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(
        label="Correo electrónico",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Correo electrónico",
                "required": "required",
            }
        ),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Contraseña",
                "required": "required",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data
    
    
    


class CustomUserLoginForm(AuthenticationForm):
    pass
