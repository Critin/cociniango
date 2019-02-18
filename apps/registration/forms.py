from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'gender',
            'age',
        ]

        labels = {
            'gender': 'Género',
            'age': 'Edad',
        }

        widgets = {
            'gender': forms.Select(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
        }