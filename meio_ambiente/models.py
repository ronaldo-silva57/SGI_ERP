from django.db import models
from usuarios.models import UsuarioCustomizado

class AspectoImpactoAmbiental(models.Model):
    NIVEL_SIGNIFICANCIA = [
        ('baixo', 'Baixo'),
        ('medio', 'Médio'),
        ('alto', 'Alto'),
        ('critico', 'Crítico'),
    ]

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('controlado', 'Controlado'),
        ('eliminado', 'Eliminado'),
    ]

    processo = models.CharField(max_length=200, help_text="Processo ou atividade analisada")
    aspecto = models.CharField(max_length=200, help_text="Ex: Consumo de energia, emissão de gases")
    impacto = models.CharField(max_length=200, help_text="Ex: Poluição atmosférica, uso de recursos naturais")
    nivel_significancia = models.CharField(max_length=20, choices=NIVEL_SIGNIFICANCIA)
    medidas_controle = models.TextField(blank=True, help_text="Controles existentes ou planejados")
    legislacao_aplicavel = models.TextField(blank=True, help_text="Legislação e requisitos aplicáveis")
    responsavel = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')
    data_avaliacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Aspecto e Impacto Ambiental"
        verbose_name_plural = "Aspectos e Impactos Ambientais"
        ordering = ['-data_avaliacao']

    def __str__(self):
        return f"{self.processo} - {self.aspecto} ({self.nivel_significancia})"


class LicencaAmbiental(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    orgao_emissor = models.CharField(max_length=150)
    validade = models.DateField()
    arquivo = models.FileField(upload_to='licencas_ambientais/', blank=True, null=True)
    observacoes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Licença Ambiental"
        verbose_name_plural = "Licenças Ambientais"

    def __str__(self):
        return f"Licença {self.numero} - {self.orgao_emissor}"


class EmergenciaAmbiental(models.Model):
    tipo_evento = models.CharField(max_length=200, help_text="Ex: Vazamento de óleo, incêndio")
    local = models.CharField(max_length=200)
    data = models.DateField()
    medidas_adotadas = models.TextField()
    responsavel = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT)
    evidencias = models.FileField(upload_to='emergencias_ambientais/', blank=True, null=True)

    class Meta:
        verbose_name = "Emergência Ambiental"
        verbose_name_plural = "Emergências Ambientais"

    def __str__(self):
        return f"{self.tipo_evento} - {self.data}"
