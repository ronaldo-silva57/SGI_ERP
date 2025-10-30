from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioCustomizado

@admin.register(UsuarioCustomizado)
class UsuarioCustomizadoAdmin(UserAdmin):
    list_display = ['username', 'email', 'get_full_name', 'tipo_usuario', 'departamento', 'is_active']
    list_filter = ['tipo_usuario', 'departamento', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo_usuario', 'departamento', 'telefone')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo_usuario', 'departamento', 'telefone', 'email')
        }),
    )