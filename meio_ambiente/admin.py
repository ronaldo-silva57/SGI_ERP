from django.contrib import admin
from .models import AspectoImpactoAmbiental, LicencaAmbiental, EmergenciaAmbiental
from simple_history.admin import SimpleHistoryAdmin

@admin.register(AspectoImpactoAmbiental)
class AspectoImpactoAmbientalAdmin(SimpleHistoryAdmin):
    list_display = ['processo', 'aspecto', 'impacto', 'nivel_significancia', 'responsavel', 'status', 'data_avaliacao']
    list_filter = ['nivel_significancia', 'status', 'data_avaliacao', 'responsavel']
    search_fields = ['processo', 'aspecto', 'impacto', 'medidas_controle']
    list_editable = ['status']
    readonly_fields = ['data_avaliacao']
    
    fieldsets = (
        ('Informações do Aspecto/Impacto', {
            'fields': ('processo', 'aspecto', 'impacto', 'nivel_significancia')
        }),
        ('Gestão e Controle', {
            'fields': ('medidas_controle', 'legislacao_aplicavel', 'responsavel', 'status')
        }),
        ('Metadados', {
            'fields': ('data_avaliacao',),
            'classes': ('collapse',)
        }),
    )

@admin.register(LicencaAmbiental)
class LicencaAmbientalAdmin(SimpleHistoryAdmin):
    list_display = ['numero', 'orgao_emissor', 'validade', 'esta_valida']
    list_filter = ['orgao_emissor', 'validade']
    search_fields = ['numero', 'orgao_emissor', 'observacoes']
    date_hierarchy = 'validade'
    
    def esta_valida(self, obj):
        from django.utils import timezone
        return obj.validade >= timezone.now().date()
    esta_valida.boolean = True
    esta_valida.short_description = 'Válida'

@admin.register(EmergenciaAmbiental)
class EmergenciaAmbientalAdmin(SimpleHistoryAdmin):
    list_display = ['tipo_evento', 'local', 'data', 'responsavel']
    list_filter = ['tipo_evento', 'data']
    search_fields = ['tipo_evento', 'local', 'medidas_adotadas']
    date_hierarchy = 'data'