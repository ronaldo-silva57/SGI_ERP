from django import forms
from .models import PerigoRisco, Acidente, TreinamentoSST

class PerigoRiscoForm(forms.ModelForm):
    class Meta:
        model = PerigoRisco
        fields = ['atividade', 'perigo', 'risco', 'nivel_risco', 'medidas_controle', 'responsavel', 'status']
        widgets = {
            'medidas_controle': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Descreva as medidas de controle existentes ou planejadas...'
            }),
        }

class AcidenteForm(forms.ModelForm):
    class Meta:
        model = Acidente
        fields = [
            'tipo', 'data', 'local', 'descricao', 'vitima', 'testemunhas',
            'causa_raiz', 'medidas_corretivas', 'evidencias'
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Descreva detalhadamente o acidente/incidente...'
            }),
            'causa_raiz': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Análise da causa raiz do evento...'
            }),
            'medidas_corretivas': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Medidas corretivas e preventivas adotadas...'
            }),
        }

class TreinamentoSSTForm(forms.ModelForm):
    class Meta:
        model = TreinamentoSST
        fields = ['nome', 'descricao', 'data', 'participantes', 'instrutor', 'certificado']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Descrição do conteúdo do treinamento...'
            }),
        }