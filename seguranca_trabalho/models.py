from django.db import models
from usuarios.models import UsuarioCustomizado

class PerigoRisco(models.Model):
    NIVEL_RISCO_CHOICES = [
        ('baixo', 'Baixo'),
        ('medio', 'Médio'),
        ('alto', 'Alto'),
        ('critico', 'Crítico'),
    ]

    STATUS_CHOICES = [
        ('identificado', 'Identificado'),
        ('controlado', 'Controlado'),
        ('eliminado', 'Eliminado'),
    ]

    atividade = models.CharField(max_length=200)
    perigo = models.CharField(max_length=200, help_text="Ex: Queda, choque elétrico, ruído, produto químico")
    risco = models.CharField(max_length=200, help_text="Ex: Fratura, queimadura, perda auditiva")
    nivel_risco = models.CharField(max_length=20, choices=NIVEL_RISCO_CHOICES)
    medidas_controle = models.TextField(blank=True)
    responsavel = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='identificado')
    data_identificacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Perigo e Risco"
        verbose_name_plural = "Perigos e Riscos"
        ordering = ['-data_identificacao']

    def __str__(self):
        return f"{self.atividade} - {self.perigo} ({self.nivel_risco})"


class Acidente(models.Model):
    TIPO_CHOICES = [
        ('acidente', 'Acidente'),
        ('incidente', 'Incidente sem lesão'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='acidente')
    data = models.DateField()
    local = models.CharField(max_length=200)
    descricao = models.TextField()
    vitima = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='vitima', null=True, blank=True)
    testemunhas = models.ManyToManyField(UsuarioCustomizado, related_name='testemunhas', blank=True)
    causa_raiz = models.TextField(blank=True)
    medidas_corretivas = models.TextField(blank=True)
    evidencias = models.FileField(upload_to='acidentes/', blank=True, null=True)

    class Meta:
        verbose_name = "Acidente / Incidente"
        verbose_name_plural = "Acidentes e Incidentes"
        ordering = ['-data']

    def __str__(self):
        return f"{self.tipo.capitalize()} em {self.local} - {self.data}"


class TreinamentoSST(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    participantes = models.ManyToManyField(UsuarioCustomizado, related_name='treinamentos_sst')
    instrutor = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='treinamentos_ministrados')
    certificado = models.FileField(upload_to='certificados_sst/', blank=True, null=True)

    class Meta:
        verbose_name = "Treinamento SST"
        verbose_name_plural = "Treinamentos SST"
        ordering = ['-data']

    def __str__(self):
        return f"{self.nome} - {self.data}"
