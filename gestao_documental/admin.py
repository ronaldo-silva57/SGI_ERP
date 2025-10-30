from django.contrib import admin
from .models import CategoriaDocumento, Documento

@admin.register(CategoriaDocumento)
class CategoriaDocumentoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'descricao_curta', 'total_documentos']
    search_fields = ['nome', 'codigo', 'descricao']
    list_filter = ['codigo']
    ordering = ['codigo']
    
    def descricao_curta(self, obj):
        return obj.descricao[:50] + '...' if len(obj.descricao) > 50 else obj.descricao
    descricao_curta.short_description = 'Descrição'
    
    def total_documentos(self, obj):
        return obj.documento_set.count()
    total_documentos.short_description = 'Total Documentos'

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'tipo_documento', 'norma', 'titulo_curto', 'categoria', 'revisao', 'status', 'data_elaboracao']
    list_filter = ['norma', 'status', 'categoria', 'tipo_documento', 'data_elaboracao']
    search_fields = ['codigo', 'titulo', 'elaborador__username', 'categoria__nome']
    readonly_fields = ['data_elaboracao']
    fieldsets = (
        ('Identificação', {
            'fields': ('codigo', 'tipo_documento', 'norma', 'titulo', 'categoria', 'revisao')
        }),
        ('Status e Controle', {
            'fields': ('status', 'data_elaboracao', 'data_aprovacao', 'controle_alteracoes')
        }),
        ('Responsáveis', {
            'fields': ('elaborador', 'aprovador')
        }),
        ('Arquivos e Versões', {
            'fields': ('arquivo', 'versao_anterior')
        }),
    )
    
    def titulo_curto(self, obj):
        return obj.titulo[:50] + '...' if len(obj.titulo) > 50 else obj.titulo
    titulo_curto.short_description = 'Título'