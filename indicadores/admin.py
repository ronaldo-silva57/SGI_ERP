from django.contrib import admin
from .models import Indicador, MedicaoIndicador

class MedicaoIndicadorInline(admin.TabularInline):
    model = MedicaoIndicador
    extra = 1

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'meta', 'unidade_medida', 'frequencia_medicao']
    list_filter = ['tipo', 'frequencia_medicao']
    search_fields = ['nome']
    inlines = [MedicaoIndicadorInline]

@admin.register(MedicaoIndicador)
class MedicaoIndicadorAdmin(admin.ModelAdmin):
    list_display = ['indicador', 'data_medicao', 'valor_medio']
    list_filter = ['data_medicao', 'indicador']
    search_fields = ['indicador__nome']