from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioCustomizado(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('gestor', 'Gestor da Qualidade'),
        ('auditor', 'Auditor Interno'),
        ('diretor', 'Diretor'),
        ('colaborador', 'Colaborador'),
    ]

    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='colaborador')
    departamento = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # CORREÇÃO AQUI
        return f"{self.get_full_name()} - {self.get_tipo_usuario_display()}"