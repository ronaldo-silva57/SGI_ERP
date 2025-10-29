from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AnaliseCritica
from .forms import AnaliseCriticaForm

class AnaliseCriticaListView(LoginRequiredMixin, ListView):
    model = AnaliseCritica
    template_name = 'analise_critica/analise_list.html'
    context_object_name = 'analises'
    paginate_by = 10
    
    def get_queryset(self):
        return AnaliseCritica.objects.all().order_by('-data_reuniao')

class AnaliseCriticaDetailView(LoginRequiredMixin, DetailView):
    model = AnaliseCritica
    template_name = 'analise_critica/analise_detail.html'
    context_object_name = 'analise'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicionar as listas processadas ao contexto
        analise = self.object
        context['kpis_list'] = analise.get_kpis_list()
        context['ncs_list'] = analise.get_ncs_list()
        context['auditorias_list'] = analise.get_auditorias_list()
        context['recursos_list'] = analise.get_recursos_list()
        context['temas_ambientais_list'] = analise._text_to_list(analise.temas_ambientais)
        context['temas_sst_list'] = analise._text_to_list(analise.temas_sst)
        return context

class AnaliseCriticaCreateView(LoginRequiredMixin, CreateView):
    model = AnaliseCritica
    form_class = AnaliseCriticaForm
    template_name = 'analise_critica/analise_form.html'
    success_url = reverse_lazy('analise-critica-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Análise crítica criada com sucesso!')
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        # Pré-selecionar o usuário atual como coordenador
        initial['coordenador'] = self.request.user
        return initial

class AnaliseCriticaUpdateView(LoginRequiredMixin, UpdateView):
    model = AnaliseCritica
    form_class = AnaliseCriticaForm
    template_name = 'analise_critica/analise_form.html'
    
    def get_success_url(self):
        return reverse_lazy('analise-critica-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Análise crítica atualizada com sucesso!')
        return super().form_valid(form)

def analise_critica_dashboard(request):
    analises_realizadas = AnaliseCritica.objects.filter(status='realizada').count()
    analises_planejadas = AnaliseCritica.objects.filter(status='planejada').count()
    ultima_analise = AnaliseCritica.objects.filter(status='realizada').order_by('-data_reuniao').first()
    
    # Estatísticas por norma
    analises_por_norma = {
        'iso9001': AnaliseCritica.objects.filter(norma='iso9001').count(),
        'iso14001': AnaliseCritica.objects.filter(norma='iso14001').count(),
        'iso45001': AnaliseCritica.objects.filter(norma='iso45001').count(),
        'integrado': AnaliseCritica.objects.filter(norma='integrado').count(),
    }
    
    context = {
        'analises_realizadas': analises_realizadas,
        'analises_planejadas': analises_planejadas,
        'ultima_analise': ultima_analise,
        'analises_por_norma': analises_por_norma,
    }
    return render(request, 'analise_critica/analise_dashboard.html', context)