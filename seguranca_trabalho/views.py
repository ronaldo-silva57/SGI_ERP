from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PerigoRisco, Acidente, TreinamentoSST
from .forms import PerigoRiscoForm, AcidenteForm, TreinamentoSSTForm

# PerigoRisco Views
class PerigoRiscoListView(LoginRequiredMixin, ListView):
    model = PerigoRisco
    template_name = 'seguranca_trabalho/perigo_list.html'
    context_object_name = 'perigos'
    paginate_by = 10

class PerigoRiscoDetailView(LoginRequiredMixin, DetailView):
    model = PerigoRisco
    template_name = 'seguranca_trabalho/perigo_detail.html'
    context_object_name = 'perigo'

class PerigoRiscoCreateView(LoginRequiredMixin, CreateView):
    model = PerigoRisco
    form_class = PerigoRiscoForm
    template_name = 'seguranca_trabalho/perigo_form.html'
    success_url = reverse_lazy('seguranca:perigo-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Perigo/Risco registrado com sucesso!')
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['responsavel'] = self.request.user
        return initial

class PerigoRiscoUpdateView(LoginRequiredMixin, UpdateView):
    model = PerigoRisco
    form_class = PerigoRiscoForm
    template_name = 'seguranca_trabalho/perigo_form.html'
    
    def get_success_url(self):
        return reverse_lazy('seguranca:perigo-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Perigo/Risco atualizado com sucesso!')
        return super().form_valid(form)

# Acidente Views
class AcidenteListView(LoginRequiredMixin, ListView):
    model = Acidente
    template_name = 'seguranca_trabalho/acidente_list.html'
    context_object_name = 'acidentes'
    paginate_by = 10

class AcidenteDetailView(LoginRequiredMixin, DetailView):
    model = Acidente
    template_name = 'seguranca_trabalho/acidente_detail.html'
    context_object_name = 'acidente'

class AcidenteCreateView(LoginRequiredMixin, CreateView):
    model = Acidente
    form_class = AcidenteForm
    template_name = 'seguranca_trabalho/acidente_form.html'
    success_url = reverse_lazy('seguranca:acidente-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Acidente/Incidente registrado com sucesso!')
        return super().form_valid(form)

class AcidenteUpdateView(LoginRequiredMixin, UpdateView):
    model = Acidente
    form_class = AcidenteForm
    template_name = 'seguranca_trabalho/acidente_form.html'
    
    def get_success_url(self):
        return reverse_lazy('seguranca:acidente-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Acidente/Incidente atualizado com sucesso!')
        return super().form_valid(form)

# TreinamentoSST Views
class TreinamentoSSTListView(LoginRequiredMixin, ListView):
    model = TreinamentoSST
    template_name = 'seguranca_trabalho/treinamento_list.html'
    context_object_name = 'treinamentos'
    paginate_by = 10

class TreinamentoSSTDetailView(LoginRequiredMixin, DetailView):
    model = TreinamentoSST
    template_name = 'seguranca_trabalho/treinamento_detail.html'
    context_object_name = 'treinamento'

class TreinamentoSSTCreateView(LoginRequiredMixin, CreateView):
    model = TreinamentoSST
    form_class = TreinamentoSSTForm
    template_name = 'seguranca_trabalho/treinamento_form.html'
    success_url = reverse_lazy('seguranca:treinamento-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Treinamento SST cadastrado com sucesso!')
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['instrutor'] = self.request.user
        return initial

class TreinamentoSSTUpdateView(LoginRequiredMixin, UpdateView):
    model = TreinamentoSST
    form_class = TreinamentoSSTForm
    template_name = 'seguranca_trabalho/treinamento_form.html'
    
    def get_success_url(self):
        return reverse_lazy('seguranca:treinamento-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Treinamento SST atualizado com sucesso!')
        return super().form_valid(form)

# Dashboard
def seguranca_trabalho_dashboard(request):
    perigos_count = PerigoRisco.objects.count()
    perigos_criticos = PerigoRisco.objects.filter(nivel_risco='critico').count()
    acidentes_count = Acidente.objects.count()
    treinamentos_count = TreinamentoSST.objects.count()
    
    context = {
        'perigos_count': perigos_count,
        'perigos_criticos': perigos_criticos,
        'acidentes_count': acidentes_count,
        'treinamentos_count': treinamentos_count,
    }
    return render(request, 'seguranca_trabalho/dashboard.html', context)