from django.db import models
from usuarios.models import UsuarioCustomizado
from simple_history.models import HistoricalRecords

class CategoriaDocumento(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Documento(models.Model):
    NORMA_CHOICES = [
        ('iso9001', 'ISO 9001 - Qualidade'),
        ('iso14001', 'ISO 14001 - Meio Ambiente'),
        ('iso45001', 'ISO 45001 - Saúde e Segurança Ocupacional'),
        ('integrado', 'Integrado (SGI)'),
    ]

    STATUS_CHOICES = [
        ('rascunho', 'Rascunho'),
        ('revisao', 'Em Revisão'),
        ('aprovado', 'Aprovado'),
        ('obsoleto', 'Obsoleto'),
    ]

    TIPO_CHOICES = [
        ('PO', 'Política'),
        ('MQ', 'Manual'),
        ('PR', 'Procedimento'),
        ('IT', 'Instrução de Trabalho'),
        ('POP', 'Procedimento Operacional Padrão'),
        ('FM', 'Formulário'),
        ('RG', 'Registro'),
        ('OT', 'Outro'),    
    ]
    
    codigo = models.CharField(max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=5, choices=TIPO_CHOICES, default='PR')
    norma = models.CharField(max_length=20, choices=NORMA_CHOICES, default='iso9001')
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaDocumento, on_delete=models.PROTECT)
    revisao = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='rascunho')
    arquivo = models.FileField(upload_to='documentos/', blank=True, null=True)
    data_elaboracao = models.DateField(auto_now_add=True)
    data_aprovacao = models.DateField(null=True, blank=True)
    elaborador = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='documentos_elaborados')
    aprovador = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='documentos_aprovados', null=True, blank=True)
    controle_alteracoes = models.TextField(help_text="Registro de alterações entre revisões", blank=True)
    versao_anterior = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    elaborador = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='documentos_elaborados')
    aprovador = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='documentos_aprovados', null=True, blank=True)
    history = HistoricalRecords(
        table_name='gestao_documental_history',
        custom_model_name=lambda x: f'Historical{x}',
        related_name='+'
    )

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ['-data_elaboracao']

    def delete(self, *args, **kwargs):
        if self.status == 'aprovado':
            self.status = 'obsoletp'
            self.ativo = False
            self.save()
        else:
            super().delete(*args, **kwargs)
    
    def __str__(self):
        return f"{self.codigo} - Rev. {self.revisao} - {self.titulo}"