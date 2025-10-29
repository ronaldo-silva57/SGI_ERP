from django.db import models

class Indicador(models.Model):
    NORMA_CHOICES = [
    ('iso9001', 'ISO 9001 - Qualidade'),
    ('iso14001', 'ISO 14001 - Meio Ambiente'),
    ('iso45001', 'ISO 45001 - Saúde e Segurança Ocupacional'),
    ('integrado', 'Integrado (SGI)'),
]
    
    CATEGORIA_CHOICES = [
        ('qualidade', 'Qualidade'),
        ('ambiental', 'Ambiental'),
        ('sst', "Saúde e Segurança"),
    ]

    TIPO_CHOICES = [
        ('eficacia', 'Eficácia'),
        ('eficiencia', 'Eficiência'),
        ('qualidade', 'Qualidade'),
        ('satisfacao', 'Satisfação'),
    ]

    nome = models.CharField(max_length=200)
    norma = models.CharField(max_length=20, choices=NORMA_CHOICES, default='iso9001')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='qualidade')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    formula_calculo = models.TextField()
    meta = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField(max_length=50)
    frequencia_medicao = models.CharField(max_length=50) #Mensal, trimestral, etc.
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.unidade_medida})"
    
class MedicaoIndicador(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    data_medicao = models.DateField()
    valor_medio = models.DecimalField(max_digits=10,decimal_places=2)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.indicador.nome} - {self.data_medicao}: {self.valor_medio}"