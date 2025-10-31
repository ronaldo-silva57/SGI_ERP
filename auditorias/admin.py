from django.contrib import admin
from .models import ProgramaAuditoria, Auditoria
from simple_history.admin import SimpleHistoryAdmin

@admin.register(ProgramaAuditoria)
class ProgramaAuditoriaAdmin(SimpleHistoryAdmin):
    list_display = ['ano', 'objetivo']
    list_filter = ['ano']
    history_list_display = ['ano', 'objetivo']

@admin.register(Auditoria)
class AuditoriaAdmin(SimpleHistoryAdmin):
    list_display = ['numero', 'programa', 'setor_auditado', 'data_planejada', 'status', 'lider']
    list_filter = ['status', 'programa', 'setor_auditado']
    search_fields = ['numero', 'setor_auditado']
    filter_horizontal = ['auditores']
    history_list_display = ['numero', 'status', 'data_planejada']
