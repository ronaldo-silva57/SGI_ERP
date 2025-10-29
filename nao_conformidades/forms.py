from django import forms
from .models import NaoConformidade

class NaoConformidadeForm(forms.ModelForm):
    class Meta:
        model = NaoConformidade
        fields = [
            'titulo', 'descricao', 'setor_envolvido', 'data_deteccao',
            'data_limite', 'gravidade', 'detectado_por', 'responsavel_analise',
            'causa_raiz', 'acao_corretiva', 'data_implementacao', 'status', 'eficaz', 'evidencias'
        ]
        widgets = {
            'data_deteccao': forms.DateInput(attrs={'type': 'date'}),
            'data_limite': forms.DateInput(attrs={'type': 'date'}),
            'data_implementacao': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'causa_raiz': forms.Textarea(attrs={'rows': 4}),
            'acao_corretiva': forms.Textarea(attrs={'rows': 4}),
        }