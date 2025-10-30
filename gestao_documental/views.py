from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Count
from .models import Documento, CategoriaDocumento
from .forms import DocumentoForm, CategoriaDocumentoForm

class DocumentoListView(ListView):
    model = Documento
    template_name = 'gestao_documental/documento_list.html'
    context_object_name = 'documentos'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Documento.objects.all()
        norma = self.request.GET.get('norma')
        status = self.request.GET.get('status')
        categoria = self.request.GET.get('categoria')
        tipo_documento = self.request.GET.get('tipo_documento')
        
        if norma:
            queryset = queryset.filter(norma=norma)
        if status:
            queryset = queryset.filter(status=status)
        if categoria:
            queryset = queryset.filter(categoria_id=categoria)
        if tipo_documento:
            queryset = queryset.filter(tipo_documento=tipo_documento)
            
        return queryset.order_by('-data_elaboracao')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = CategoriaDocumento.objects.all()
        return context

class DocumentoDetailView(DetailView):
    model = Documento
    template_name = 'gestao_documental/documento_detail.html'
    context_object_name = 'documento'

class DocumentoCreateView(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'gestao_documental/documento_form.html'
    success_url = reverse_lazy('gestao_documental:documento-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Documento criado com sucesso!')
        return super().form_valid(form)

class DocumentoUpdateView(UpdateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'gestao_documental/documento_form.html'
    
    def get_success_url(self):
        return reverse_lazy('gestao_documental:documento-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Documento atualizado com sucesso!')
        return super().form_valid(form)

# Views para CategoriaDocumento
class CategoriaDocumentoListView(ListView):
    model = CategoriaDocumento
    template_name = 'gestao_documental/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

class CategoriaDocumentoCreateView(CreateView):
    model = CategoriaDocumento
    form_class = CategoriaDocumentoForm
    template_name = 'gestao_documental/categoria_form.html'
    success_url = reverse_lazy('gestao_documental:categoria-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoria criada com sucesso!')
        return super().form_valid(form)

class CategoriaDocumentoUpdateView(UpdateView):
    model = CategoriaDocumento
    form_class = CategoriaDocumentoForm
    template_name = 'gestao_documental/categoria_form.html'
    success_url = reverse_lazy('gestao_documental:categoria-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoria atualizada com sucesso!')
        return super().form_valid(form)

class CategoriaDocumentoDeleteView(DeleteView):
    model = CategoriaDocumento
    template_name = 'gestao_documental/categoria_confirm_delete.html'
    success_url = reverse_lazy('gestao_documental:categoria-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Categoria excluída com sucesso!')
        return super().delete(request, *args, **kwargs)

@login_required
def documento_dashboard(request):
    total_documentos = Documento.objects.count()
    documentos_aprovados = Documento.objects.filter(status='aprovado').count()
    documentos_revisao = Documento.objects.filter(status='revisao').count()
    
    # Estatísticas por norma
    normas_stats = {}
    for norma_code, norma_name in Documento.NORMA_CHOICES:
        count = Documento.objects.filter(norma=norma_code).count()
        normas_stats[norma_name] = count
    
    # Estatísticas por categoria
    categorias_stats = CategoriaDocumento.objects.annotate(
        total_documentos=Count('documento')
    ).values('nome', 'total_documentos')
    
    # Estatísticas por tipo de documento
    tipos_stats = {}
    for tipo_code, tipo_name in Documento.TIPO_CHOICES:
        count = Documento.objects.filter(tipo_documento=tipo_code).count()
        tipos_stats[tipo_name] = count

    context = {
        'total_documentos': total_documentos,
        'documentos_aprovados': documentos_aprovados,
        'documentos_revisao': documentos_revisao,
        'normas_stats': normas_stats,
        'categorias_stats': categorias_stats,
        'tipos_stats': tipos_stats,
    }
    return render(request, 'gestao_documental/documento_dashboard.html', context)

def get_categoria_documentos(request, categoria_id):
    """Retorna documentos por categoria para AJAX"""
    documentos = Documento.objects.filter(categoria_id=categoria_id).values('id', 'codigo', 'titulo')
    return JsonResponse(list(documentos), safe=False)