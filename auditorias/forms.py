from django import forms
from .models import ProgramaAuditoria, Auditoria

class ProgramaAuditoriaForm(forms.ModelForm):
    class Meta:
        model = ProgramaAuditoria
        fields = ['ano', 'objetivo', 'escopo', 'criterios']
        widgets = {
            'objetivo': forms.Textarea(attrs={'rows': 3}),
            'escopo': forms.Textarea(attrs={'rows': 3}),
            'criterios': forms.Textarea(attrs={'rows': 3}),
        }

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = [
            'programa', 'data_planejada', 'data_realizada', 
            'setor_auditado', 'auditores', 'lider', 'status', 'relatorio'
        ]
        widgets = {
            'data_planejada': forms.DateInput(attrs={'type': 'date'}),
            'data_realizacao': forms.DateInput(attrs={'type': 'date'}),
        }