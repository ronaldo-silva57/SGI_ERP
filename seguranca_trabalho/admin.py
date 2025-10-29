from django.contrib import admin
from .models import PerigoRisco, Acidente, TreinamentoSST

#@admin.register(PerigoRisco)
class PerigoRiscoAdmin(admin.ModelAdmin):
    list_display = ['atividade', 'perigo', 'risco', 'nivel_risco', 'responsavel', 'status', 'data_identificacao']
    list_filter = ['nivel_risco', 'status', 'data_identificacao', 'responsavel']
    search_fields = ['atividade', 'perigo', 'risco', 'medidas_controle']
    list_editable = ['status']
    readonly_fields = ['data_identificacao']
    
    fieldsets = (
        ('Identificação do Perigo/Risco', {
            'fields': ('atividade', 'perigo', 'risco', 'nivel_risco')
        }),
        ('Gestão do Risco', {
            'fields': ('medidas_controle', 'responsavel', 'status')
        }),
        ('Metadados', {
            'fields': ('data_identificacao',),
            'classes': ('collapse',)
        }),
    )

#@admin.register(Acidente)
class AcidenteAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'data', 'local', 'vitima', 'causa_raiz_breve']
    list_filter = ['tipo', 'data']
    search_fields = ['local', 'descricao', 'causa_raiz']
    date_hierarchy = 'data'
    filter_horizontal = ['testemunhas']
    
    def causa_raiz_breve(self, obj):
        return obj.causa_raiz[:50] + '...' if obj.causa_raiz and len(obj.causa_raiz) > 50 else obj.causa_raiz
    causa_raiz_breve.short_description = 'Causa Raiz'

#@admin.register(TreinamentoSST)
class TreinamentoSSTAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data', 'instrutor', 'participantes_count']
    list_filter = ['data', 'instrutor']
    search_fields = ['nome', 'descricao']
    date_hierarchy = 'data'
    filter_horizontal = ['participantes']
    
    def participantes_count(self, obj):
        return obj.participantes.count()
    participantes_count.short_description = 'Participantes'