from django.db import models
from usuarios.models import UsuarioCustomizado

class ProgramaAuditoria(models.Model):
    ano = models.IntegerField()
    objetivo = models.TextField()
    escopo = models.TextField()
    criterios = models.TextField()

    def __str__(self):
        return f"Programa de Auditoria {self.ano}"

class Auditoria(models.Model):
    NORMA_CHOICES = [
        ('iso9001', 'ISO 9001 - Qualidade'),
        ('iso14001', 'ISO 14001 - Meio Ambiente'),
        ('iso45001', 'ISO 45001 - Saúde e Segurança Ocupacional'),
        ('integrado', 'Integrado (SGI)'),
    ]

    TIPO_AUDITORIA_CHOICES = [
        ('qualidade', 'Qualidade (ISO 9001)'),
        ('ambiental', 'Meio Ambiente (ISO 14001)'),
        ('sst', 'Saúde e Segurança (ISO 45001)'),
        ('integrada', 'Integrada (SGI)'),
    ]

    STATUS_CHOICE = [
        ('planejada', 'Planejada'),
        ('executada', 'Em Execução'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]

    numero = models.CharField(max_length=15, unique=True)
    norma = models.CharField(max_length=20, choices=NORMA_CHOICES, default='iso9001')
    tipo = models.CharField(max_length=20, choices=TIPO_AUDITORIA_CHOICES, default='qualidade')
    programa = models .ForeignKey(ProgramaAuditoria, on_delete=models.PROTECT)
    data_planejada = models.DateField()
    data_realizada = models.DateField(null=True, blank=True)
    setor_auditado = models.CharField(max_length=100)
    auditores = models.ManyToManyField(UsuarioCustomizado, related_name='auditorias')
    lider = models.ForeignKey(UsuarioCustomizado, on_delete=models.PROTECT, related_name='auditorias_lideradas')
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='planejada')
    relatorio = models.FileField(upload_to='relatorios_auditoria/', blank=True)

    class Meta:
        verbose_name = "Auditoria"
        verbose_name_plural = "Auditorias"

    def __str__(self):
        return f"Auditoria {self.numero} - {self.setor_auditado}"