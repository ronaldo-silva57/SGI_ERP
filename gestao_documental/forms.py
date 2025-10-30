# forms.py - ATUALIZADO
from django import forms
from .models import Documento, CategoriaDocumento

class CategoriaDocumentoForm(forms.ModelForm):
    class Meta:
        model = CategoriaDocumento
        fields = ['codigo', 'nome', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'codigo', 'norma', 'titulo', 'categoria', 'revisao', 'status',
            'arquivo', 'data_aprovacao', 'elaborador', 'aprovador',
            'controle_alteracoes'
        ]
        widgets = {
            'data_aprovacao': forms.DateInput(attrs={'type': 'date'}),
            'controle_alteracoes': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_aprovacao'].required = False
        self.fields['arquivo'].required = False