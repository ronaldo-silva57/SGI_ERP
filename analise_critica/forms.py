from django import forms
from .models import AnaliseCritica

class AnaliseCriticaForm(forms.ModelForm):
    class Meta:
        model = AnaliseCritica
        fields = [
            'periodo', 'norma', 'data_reuniao', 'data_proxima_reuniao', 'coordenador',
            'participantes', 'status', 'kpis_analisados', 'ncs_analisadas',
            'auditorias_analisadas', 'recursos_necessarios', 'decisoes_tomadas',
            'acoes_melhoria', 'observacoes', 'ata_reuniao', 'temas_ambientais', 'temas_sst'
        ]
        widgets = {
            'data_reuniao': forms.DateInput(attrs={'type': 'date'}),
            'data_proxima_reuniao': forms.DateInput(attrs={'type': 'date'}),
            'decisoes_tomadas': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva as decisões tomadas durante a reunião...'}),
            'acoes_melhoria': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva as ações de melhoria definidas...'}),
            'observacoes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Observações adicionais...'}),
            'temas_ambientais': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Digite um aspecto/impacto ambiental por linha:\nEx: Consumo de água - Redução do recurso hídrico\nEmissões de CO2 - Contribuição para mudanças climáticas'
            }),
            'temas_sst': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Digite um risco/oportunidade de SST por linha:\nEx: Queda de altura - Implementação de proteções coletivas\nErgonomia - Melhoria no layout de trabalho'
            }),
            'kpis_analisados': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Digite um KPI por linha:\nEx: Taxa de conformidade - 95%\nTempo de resposta - 24h'
            }),
            'ncs_analisadas': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Digite uma NC por linha:\nEx: NC-001 - Produto não conforme\nNC-002 - Documentação incompleta'
            }),
            'auditorias_analisadas': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Digite uma auditoria por linha:\nEx: AUD-001 - Auditoria Produção\nAUD-002 - Auditoria Qualidade'
            }),
            'recursos_necessarios': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Digite um recurso por linha:\nEx: Treinamento em ISO 9001:2015\nSoftware de gestão documental'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Atualizar os help texts
        self.fields['kpis_analisados'].help_text = "Digite um indicador por linha"
        self.fields['ncs_analisadas'].help_text = "Digite uma não conformidade por linha"
        self.fields['auditorias_analisadas'].help_text = "Digite uma auditoria por linha"
        self.fields['recursos_necessarios'].help_text = "Digite um recurso necessário por linha"
        self.fields['temas_ambientais'].help_text = "Digite um aspecto/impacto ambiental por linha"
        self.fields['temas_sst'].help_text = "Digite um risco/oportunidade de SST por linha"