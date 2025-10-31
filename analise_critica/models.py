from django.db import models
from usuarios.models import UsuarioCustomizado
from simple_history.models import HistoricalRecords

class AnaliseCritica(models.Model):
    NORMA_CHOICES = [
        ('iso9001', 'ISO 9001 - Qualidade'),
        ('iso14001', 'ISO 14001 - Meio Ambiente'),
        ('iso45001', 'ISO 45001 - Saúde e Segurança Ocupacional'),
        ('integrado', 'Integrado (SGI)'),
    ]

    STATUS_CHOICES = [
        ('planejada', 'Planejada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]
 
    periodo = models.CharField(max_length=50, help_text="Ex: 1º Trimestre 2024")
    norma = models.CharField(max_length=20, choices=NORMA_CHOICES, default='iso9001')
    data_reuniao = models.DateField()
    data_proxima_reuniao = models.DateField()
    participantes = models.ManyToManyField(
        UsuarioCustomizado,
        related_name='analises_criticas'
    )
    coordenador = models.ForeignKey(
        UsuarioCustomizado,
        on_delete=models.PROTECT,
        related_name='analises_coordenadas'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planejada')

    # Campos de texto simples (um item por linha)
    kpis_analisados = models.TextField(
        help_text="Indicadores analisados (um por linha)", 
        blank=True, 
        null=True
    )
    ncs_analisadas = models.TextField(
        help_text="Não conformidades analisadas (uma por linha)", 
        blank=True, 
        null=True
    )
    auditorias_analisadas = models.TextField(
        help_text="Auditorias analisadas (uma por linha)", 
        blank=True, 
        null=True
    )
    recursos_necessarios = models.TextField(
        help_text="Recursos necessários identificados (um por linha)", 
        blank=True, 
        null=True
    )

    # Decisões e ações
    decisoes_tomadas = models.TextField()
    acoes_melhoria = models.TextField()
    observacoes = models.TextField(blank=True)
    ata_reuniao = models.FileField(upload_to='atas_analise_critica/', blank=True)
    temas_ambientais = models.TextField(blank=True, help_text="Aspectos e impactos ambientais discutidos")
    temas_sst = models.TextField(blank=True, help_text="Riscos e oportunidades de SST abordados")

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(
        table_name='analise_critica_history',
        custom_model_name=lambda x: f'Historical{x}',
        related_name='+'
    )
    class Meta:
        verbose_name = "Análise Crítica"
        verbose_name_plural = "Análises Críticas"
        ordering = ['-data_reuniao']

    def __str__(self):
        return f"Análise Crítica - {self.periodo}"

    # Métodos auxiliares para trabalhar com listas
    def get_kpis_list(self):
        """Retorna a lista de KPIs analisados"""
        return self._text_to_list(self.kpis_analisados)
    
    def get_ncs_list(self):
        """Retorna a lista de NCs analisadas"""
        return self._text_to_list(self.ncs_analisadas)
    
    def get_auditorias_list(self):
        """Retorna a lista de auditorias analisadas"""
        return self._text_to_list(self.auditorias_analisadas)
    
    def get_recursos_list(self):
        """Retorna a lista de recursos necessários"""
        return self._text_to_list(self.recursos_necessarios)
    
    def _text_to_list(self, text_field):
        """Converte texto (um item por linha) em lista, removendo linhas vazias"""
        if not text_field:
            return []
        return [item.strip() for item in text_field.split('\n') if item.strip()]