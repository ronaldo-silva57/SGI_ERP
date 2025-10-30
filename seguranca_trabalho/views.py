from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PerigoRisco, Acidente, TreinamentoSST
from .forms import PerigoRiscoForm, AcidenteForm, TreinamentoSSTForm

# PerigoRisco Views
#class PerigoRiscoListView(LoginRequiredMixin, ListView):
class PerigoRiscoListView(ListView):
    model = PerigoRisco
    template_name = 'seguranca_trabalho/perigo_list.html'
    context_object_name = 'perigos'
    paginate_by = 10

#class PerigoRiscoDetailView(LoginRequiredMixin, DetailView):
class PerigoRiscoDetailView(DetailView):
    model = PerigoRisco
    template_name = 'seguranca_trabalho/perigo_detail.html'
    context_object_name = 'perigo'

#class PerigoRiscoCreateView(LoginRequiredMixin, CreateView):
class PerigoRiscoCreateView(CreateView):
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

#class PerigoRiscoUpdateView(LoginRequiredMixin, UpdateView):
class PerigoRiscoUpdateView(UpdateView):
    model = PerigoRisco
    form_class = PerigoRiscoForm
    template_name = 'seguranca_trabalho/perigo_form.html'
    
    def get_success_url(self):
        return reverse_lazy('seguranca:perigo-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Perigo/Risco atualizado com sucesso!')
        return super().form_valid(form)

# Acidente Views
#class AcidenteListView(LoginRequiredMixin, ListView):
class AcidenteListView(ListView):
    model = Acidente
    template_name = 'seguranca_trabalho/acidente_list.html'
    context_object_name = 'acidentes'
    paginate_by = 10

#class AcidenteDetailView(LoginRequiredMixin, DetailView):
class AcidenteDetailView(DetailView):
    model = Acidente
    template_name = 'seguranca_trabalho/acidente_detail.html'
    context_object_name = 'acidente'

#class AcidenteCreateView(LoginRequiredMixin, CreateView):
class AcidenteCreateView(CreateView):
    model = Acidente
    form_class = AcidenteForm
    template_name = 'seguranca_trabalho/acidente_form.html'
    success_url = reverse_lazy('seguranca:acidente-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Acidente/Incidente registrado com sucesso!')
        return super().form_valid(form)

#class AcidenteUpdateView(LoginRequiredMixin, UpdateView):
class AcidenteUpdateView(UpdateView):
    model = Acidente
    form_class = AcidenteForm
    template_name = 'seguranca_trabalho/acidente_form.html'
    
    def get_success_url(self):
        return reverse_lazy('seguranca:acidente-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Acidente/Incidente atualizado com sucesso!')
        return super().form_valid(form)

# TreinamentoSST Views
#class TreinamentoSSTListView(LoginRequiredMixin, ListView):
class TreinamentoSSTListView(ListView):
    model = TreinamentoSST
    template_name = 'seguranca_trabalho/treinamento_list.html'
    context_object_name = 'treinamentos'
    paginate_by = 10

#class TreinamentoSSTDetailView(LoginRequiredMixin, DetailView):
class TreinamentoSSTDetailView(DetailView):
    model = TreinamentoSST
    template_name = 'seguranca_trabalho/treinamento_detail.html'
    context_object_name = 'treinamento'

#class TreinamentoSSTCreateView(LoginRequiredMixin, CreateView):
class TreinamentoSSTCreateView(CreateView):
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

#class TreinamentoSSTUpdateView(UpdateView):
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

def perigo_list(request):
    perigos = PerigoRisco.objects.all()

    nivel_risco = request.GET.get('nivel_risco')
    status = request.GET.get('status')
    atividade = request.GET.get('atividade')

    if nivel_risco:
        perigos = perigos.filter(nivel_risco=nivel_risco)
    if status:
        perigos = perigos.filter(status=status)
    if atividade:
        perigos = perigos.filter(atividade__icontains=atividade)

    context = {
        'perigos': perigos,
    }
    return render(request, 'seguranca_trabalho/perigo_list.html', context)

from django.utils import timezone

def acidente_list(request):
    acidentes = Acidente.objects.all()

    tipo = request.GET.get('tipo')
    local = request.GET.get('local')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if tipo:
        acidentes = acidentes.filter(tipo=tipo)
    if local:
        acidentes = acidentes.filter(local__icontains=local)
    if data_inicio:
        acidentes = acidentes.filter(data__gte=data_inicio)
    if data_fim:
        acidentes = acidentes.filter(data__lte=data_fim)

    context = {
        'acidentes': acidentes,
        'today': timezone.now().date(),
    }
    return render(request, 'seguranca_trabalho/acidente_list.html', context)

def treinamento_list(request):
    treinamentos = TreinamentoSST.objects.all()

    nome = request.GET.get('nome')
    instrutor = request.GET.get('instrutor')
    data = request.GET.get('data')

    if nome:
        treinamentos = treinamentos.filter(nome__icontains=nome)
    if instrutor:
        treinamentos = treinamentos.filter(instrutor__first_name__icontains=instrutor)
    if data:
        treinamentos = treinamentos.filter(data=data)

    context = {
        'treinamentos': treinamentos,
    }
    return render(request, 'seguranca_trabalho/treinamento_list.html', context)
