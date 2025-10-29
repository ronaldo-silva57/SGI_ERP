from django.contrib import admin
from .models import NaoConformidade

@admin.register(NaoConformidade)
class NaoConformidadeAdmin(admin.ModelAdmin):
    list_display = ['numero', 'titulo', 'setor_envolvido', 'data_deteccao', 'gravidade', 'status']
    list_filter = ['status', 'gravidade', 'setor_envolvido', 'data_deteccao']
    search_fields = ['numero', 'titulo', 'descricao']
    readonly_fields = ['data_deteccao']
    fieldsets = (
        ('Identificação', {
            'fields': ('numero', 'titulo', 'setor_envolvido')
        }),
        ('Detalhamento', {
            'fields': ('descricao', 'gravidade', 'data_deteccao', 'data_limite')
        }),
        ('Responsáveis', {
            'fields': ('detectado_por', 'responsavel_analise')
        }),
        ('Análise e Ações', {
            'fields': ('causa_raiz', 'acao_corretiva', 'data_implementacao')
        }),
        ('Resultado', {
            'fields': ('status', 'eficaz', 'evidencias')
        }),
    )