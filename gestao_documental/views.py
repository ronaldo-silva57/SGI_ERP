from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Documento, CategoriaDocumento
from .forms import DocumentoForm, CategoriaDocumentoForm

class DocumentoListView(ListView):
    model = Documento
    template_name = 'gestao_documental/documento_list.html'
    context_object_name = 'documentos'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Documento.objects.all()
        status = self.request.GET.get('status')
        categoria = self.request.GET.get('categoria')
        
        if status:
            queryset = queryset.filter(status=status)
        if categoria:
            queryset = queryset.filter(categoria_id=categoria)
            
        return queryset.order_by('-data_elaboracao')

class DocumentoDetailView(DetailView):
    model = Documento
    template_name = 'gestao_documental/documento_detail.html'
    context_object_name = 'documento'

class DocumentoCreateView(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'gestao_documental/documento_form.html'
    success_url = reverse_lazy('documento-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Documento criado com sucesso!')
        return super().form_valid(form)

class DocumentoUpdateView(UpdateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'gestao_documental/documento_form.html'
    
    def get_success_url(self):
        return reverse_lazy('documento-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Documento atualizado com sucesso!')
        return super().form_valid(form)

@login_required
def documento_dashboard(request):
    total_documentos = Documento.objects.count()
    documentos_aprovados = Documento.objects.filter(status='aprovado').count()
    documentos_revisao = Documento.objects.filter(status='revisao').count()
    
    context = {
        'total_documentos': total_documentos,
        'documentos_aprovados': documentos_aprovados,
        'documentos_revisao': documentos_revisao,
    }
    return render(request, 'gestao_documental/documento_dashboard.html', context)