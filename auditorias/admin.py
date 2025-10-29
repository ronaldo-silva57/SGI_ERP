from django.contrib import admin
from .models import ProgramaAuditoria, Auditoria

#@admin.register(ProgramaAuditoria)
class ProgramaAuditoriaAdmin(admin.ModelAdmin):
    list_display = ['ano', 'objetivo']
    list_filter = ['ano']

#@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'programa', 'setor_auditado', 'data_planejada', 'status', 'lider']
    list_filter = ['status', 'programa', 'setor_auditado']
    search_fields = ['numero', 'setor_auditado']
    filter_horizontal = ['auditores']