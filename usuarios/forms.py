from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioCustomizado

class UsuarioCustomizadoCreationForm(UserCreationForm):
    class Meta:
        model = UsuarioCustomizado
        fields = ['username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'departamento', 'telefone']
        widgets = {
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UsuarioCustomizadoChangeForm(UserChangeForm):
    class Meta:
        model = UsuarioCustomizado
        fields = ['username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'departamento', 'telefone']