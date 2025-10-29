from django import forms
from .models import AspectoImpactoAmbiental, LicencaAmbiental, EmergenciaAmbiental

class AspectoImpactoAmbientalForm(forms.ModelForm):
    class Meta:
        model = AspectoImpactoAmbiental
        fields = [
            'processo', 'aspecto', 'impacto', 'nivel_significancia',
            'medidas_controle', 'legislacao_aplicavel', 'responsavel', 'status'
        ]
        widgets = {
            'medidas_controle': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Descreva as medidas de controle existentes ou planejadas...'
            }),
            'legislacao_aplicavel': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Liste a legislação e requisitos aplicáveis...'
            }),
        }

class LicencaAmbientalForm(forms.ModelForm):
    class Meta:
        model = LicencaAmbiental
        fields = ['numero', 'orgao_emissor', 'validade', 'arquivo', 'observacoes']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

class EmergenciaAmbientalForm(forms.ModelForm):
    class Meta:
        model = EmergenciaAmbiental
        fields = ['tipo_evento', 'local', 'data', 'medidas_adotadas', 'responsavel', 'evidencias']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'medidas_adotadas': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Descreva as medidas adotadas durante a emergência...'
            }),
        }