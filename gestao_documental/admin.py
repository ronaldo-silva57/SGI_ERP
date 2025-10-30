# admin.py - ATUALIZADO
from django.contrib import admin
from .models import CategoriaDocumento, Documento

@admin.register(CategoriaDocumento)
class CategoriaDocumentoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'descricao']
    search_fields = ['nome', 'codigo']
    ordering = ['codigo']

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'norma', 'titulo', 'categoria', 'revisao', 'status', 'data_elaboracao']
    list_filter = ['norma', 'status', 'categoria', 'data_elaboracao']
    search_fields = ['codigo', 'titulo', 'elaborador__username']
    readonly_fields = ['data_elaboracao']
    fieldsets = (
        ('Identificação', {
            'fields': ('codigo', 'norma', 'titulo', 'categoria', 'revisao')
        }),
        ('Status e Controle', {
            'fields': ('status', 'data_elaboracao', 'data_aprovacao')
        }),
        ('Responsáveis', {
            'fields': ('elaborador', 'aprovador')
        }),
        ('Arquivos', {
            'fields': ('arquivo', 'controle_alteracoes')
        }),
    )