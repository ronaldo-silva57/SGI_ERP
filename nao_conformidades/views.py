from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import NaoConformidade
from .forms import NaoConformidadeForm

#class NaoConformidadeListView(LoginRequiredMixin, ListView):
class NaoConformidadeListView(ListView):
    model = NaoConformidade
    template_name = 'nao_conformidades/naoconformidade_list.html'
    context_object_name = 'nao_conformidades'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = NaoConformidade.objects.all()
        status = self.request.GET.get('status')
        gravidade = self.request.GET.get('gravidade')
        
        if status:
            queryset = queryset.filter(status=status)
        if gravidade:
            queryset = queryset.filter(gravidade=gravidade)
            
        return queryset.order_by('-data_deteccao')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicionar estatísticas para o template
        context['ncs_abertas'] = NaoConformidade.objects.filter(status='aberta').count()
        context['ncs_analise'] = NaoConformidade.objects.filter(status='analise').count()
        context['ncs_atrasadas'] = NaoConformidade.objects.filter(
            status__in=['aberta', 'analise'], 
            data_limite__lt=timezone.now()
        ).count()
        context['today'] = timezone.now().date()
        return context

#class NaoConformidadeDetailView(LoginRequiredMixin, DetailView):
class NaoConformidadeDetailView(DetailView):
    model = NaoConformidade
    template_name = 'nao_conformidades/naoconformidade_detail.html'
    context_object_name = 'nc'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

#class NaoConformidadeCreateView(LoginRequiredMixin, CreateView):
class NaoConformidadeCreateView(CreateView):
    model = NaoConformidade
    form_class = NaoConformidadeForm
    template_name = 'nao_conformidades/naoconformidade_form.html'
    success_url = reverse_lazy('nao_conformidades:nao-conformidade-list')
    
    def form_valid(self, form):
        # Gerar número automático para NC
        ultima_nc = NaoConformidade.objects.order_by('-id').first()
        if ultima_nc:
            ultimo_numero = int(ultima_nc.numero.split('-')[1])
            novo_numero = f"NC-{ultimo_numero + 1:04d}"
        else:
            novo_numero = "NC-0001"
        
        form.instance.numero = novo_numero
        messages.success(self.request, 'Não conformidade registrada com sucesso!')
        return super().form_valid(form)

#class NaoConformidadeUpdateView(LoginRequiredMixin, UpdateView):
class NaoConformidadeUpdateView(UpdateView):
    model = NaoConformidade
    form_class = NaoConformidadeForm
    template_name = 'nao_conformidades/naoconformidade_form.html'
    
    def get_success_url(self):
        return reverse_lazy('nao_conformidades:nao-conformidade-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Não conformidade atualizada com sucesso!')
        return super().form_valid(form)

def nc_dashboard(request):
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('usuarios:login')
    
    ncs_abertas = NaoConformidade.objects.filter(status='aberta').count()
    ncs_analise = NaoConformidade.objects.filter(status='analise').count()
    ncs_atrasadas = NaoConformidade.objects.filter(
        status__in=['aberta', 'analise'], 
        data_limite__lt=timezone.now()
    ).count()
    
    context = {
        'ncs_abertas': ncs_abertas,
        'ncs_analise': ncs_analise,
        'ncs_atrasadas': ncs_atrasadas,
    }
    return render(request, 'nao_conformidades/nc_dashboard.html', context)