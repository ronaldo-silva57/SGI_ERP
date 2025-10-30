from django.contrib import admin
from .models import AnaliseCritica

@admin.register(AnaliseCritica)
class AnaliseCriticaAdmin(admin.ModelAdmin):
    list_display = ['periodo', 'norma', 'data_reuniao', 'coordenador', 'status', 'data_proxima_reuniao']
    list_filter = ['norma', 'status', 'data_reuniao', 'coordenador']
    search_fields = ['periodo', 'decisoes_tomadas', 'acoes_melhoria', 'temas_ambientais', 'temas_sst']
    filter_horizontal = ['participantes']
    readonly_fields = ['data_criacao', 'data_atualizacao']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('periodo', 'norma', 'data_reuniao', 'data_proxima_reuniao', 'coordenador', 'participantes', 'status')
        }),
        ('Pontos Abordados - Qualidade', {
            'fields': ('kpis_analisados', 'ncs_analisadas', 'auditorias_analisadas', 'recursos_necessarios'),
            'description': 'Digite um item por linha nos campos abaixo'
        }),
        ('Pontos Abordados - SGI', {
            'fields': ('temas_ambientais', 'temas_sst'),
            'description': 'Aspectos ambientais e riscos de SST'
        }),
        ('Resultados', {
            'fields': ('decisoes_tomadas', 'acoes_melhoria', 'observacoes', 'ata_reuniao')
        }),
        ('Metadados', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )