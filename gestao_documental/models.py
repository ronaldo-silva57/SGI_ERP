# models.py - ATUALIZADO
from django.db import models
from usuarios.models import UsuarioCustomizado

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
    
    codigo = models.CharField(max_length=20, unique=True)
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
    
    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ['-data_elaboracao']
    
    def __str__(self):
        return f"{self.codigo} - Rev. {self.revisao} - {self.titulo}"