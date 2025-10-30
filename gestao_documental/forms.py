from django import forms
from .models import Documento, CategoriaDocumento

class CategoriaDocumentoForm(forms.ModelForm):
    class Meta:
        model = CategoriaDocumento
        fields = ['codigo', 'nome', 'descricao']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: CAT001'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da categoria'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição da categoria'}),
        }
        labels = {
            'codigo': 'Código da Categoria',
            'nome': 'Nome da Categoria',
            'descricao': 'Descrição',
        }
    
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if self.instance.pk:
            if CategoriaDocumento.objects.filter(codigo=codigo).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Este código já está em uso.')
        else:
            if CategoriaDocumento.objects.filter(codigo=codigo).exists():
                raise forms.ValidationError('Este código já está em uso.')
        return codigo

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'codigo', 'tipo_documento', 'norma', 'titulo', 'categoria', 'revisao', 'status',
            'arquivo', 'data_aprovacao', 'elaborador', 'aprovador',
            'controle_alteracoes'
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'norma': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'revisao': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'data_aprovacao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'elaborador': forms.Select(attrs={'class': 'form-control'}),
            'aprovador': forms.Select(attrs={'class': 'form-control'}),
            'controle_alteracoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_aprovacao'].required = False
        self.fields['arquivo'].required = False
        self.fields['aprovador'].required = False
        
        # Ordenar categorias por nome
        self.fields['categoria'].queryset = CategoriaDocumento.objects.all().order_by('nome')