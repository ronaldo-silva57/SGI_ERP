from django import forms
from .models import Indicador, MedicaoIndicador

class IndicadorForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = ['nome', 'tipo', 'formula_calculo', 'meta', 'unidade_medida', 'frequencia_medicao', 'responsavel']
        widgets = {
            'formula_calculo': forms.Textarea(attrs={'rows': 3}),
        }

class MedicaoIndicadorForm(forms.ModelForm):
    class Meta:
        model = MedicaoIndicador
        fields = ['indicador', 'data_medicao', 'valor_medio', 'observacoes']
        widgets = {
            'data_medicao': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }