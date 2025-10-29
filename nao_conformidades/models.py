from django.db import models
from usuarios.models import UsuarioCustomizado

class NaoConformidade(models.Model):
    NORMA_CHOICES = [
        ('iso9001', 'ISO 9001 - Qualidade'),
        ('iso14001', 'ISO 14001 - Meio Ambiente'),
        ('iso45001', 'ISO 45001 - Saúde e Segurança Ocupacional'),
        ('integrado', 'Integrado (SGI)'),
    ]

    ORIGEM_CHOICES = [
        ('produto', 'Produto / Serviço'),
        ('processo', 'Processo'),
        ('ambiental', 'Ambiental'),
        ('seguranca', 'Segurança do Trabalho'),
    ]

    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('analise', 'Em Análise'),
        ('acao_implementada', 'Ação Implementada'),
        ('Verificada', 'Eficácia Verificada'),
        ('fechada', 'Fechada'),
    ]

    GRAVIDADE_CHOICES = [
        ('baixa', 'Baixa',),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]

    numero = models.CharField(max_length=15, unique=True)
    
    titulo = models.CharField(max_length=200)
    norma = models.CharField(max_length=20, choices=NORMA_CHOICES, default='iso9001')
    descricao = models.TextField()
    setor_envolvido = models.CharField(max_length=100)
    data_deteccao = models.DateField()
    data_limite = models.DateField()
    gravidade = models.CharField(max_length=20, choices=GRAVIDADE_CHOICES, default='aberta')
    detectado_por = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='ncs_detectadas')
    responsavel_analise = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='ncs_analise')
    #campos de analise
    causa_raiz = models.TextField(blank=True)
    acao_corretiva = models.TextField(blank=True)
    data_implementacao = models.DateField(null=True, blank=True)
    eficaz = models.BooleanField(blank=True, null=True)
    evidencias = models.FileField(upload_to='evidencias_nc/', blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        verbose_name = "Não Conformidade"
        verbose_name_plural = "Não Conformidades"
        ordering = ['-data_deteccao']

    def __str__(self):
        return f"NC {self.numero} - {self.titulo}"