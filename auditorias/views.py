from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Auditoria, ProgramaAuditoria
from .forms import AuditoriaForm, ProgramaAuditoriaForm

#class AuditoriaListView(ListView):
class AuditoriaListView(LoginRequiredMixin, ListView):
    model = Auditoria
    template_name = 'auditorias/auditoria_list.html'
    context_object_name = 'auditorias'
    paginate_by = 10
    
    def get_queryset(self):
        return Auditoria.objects.all().order_by('-data_planejada')

#class AuditoriaDetailView(LoginRequiredMixin, DetailView):
class AuditoriaDetailView(DetailView):
    model = Auditoria
    template_name = 'auditorias/auditoria_detail.html'
    context_object_name = 'auditoria'

#class AuditoriaCreateView(LoginRequiredMixin, CreateView):
class AuditoriaCreateView(CreateView):
    model = Auditoria
    form_class = AuditoriaForm
    template_name = 'auditorias/auditoria_form.html'
    success_url = reverse_lazy('auditorias:auditoria-list')
    
    def form_valid(self, form):
        # Gerar número automático
        ultima_auditoria = Auditoria.objects.order_by('-id').first()
        if ultima_auditoria:
            ultimo_numero = int(ultima_auditoria.numero.split('-')[1])
            novo_numero = f"AUD-{ultimo_numero + 1:04d}"
        else:
            novo_numero = "AUD-0001"
        
        form.instance.numero = novo_numero
        messages.success(self.request, 'Auditoria criada com sucesso!')
        return super().form_valid(form)

#class AuditoriaUpdateView(LoginRequiredMixin, UpdateView):
class AuditoriaUpdateView(UpdateView):
    model = Auditoria
    form_class = AuditoriaForm
    template_name = 'auditorias/auditoria_form.html'
    
    def get_success_url(self):
        return reverse_lazy('auditorias:auditoria-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Auditoria atualizada com sucesso!')
        return super().form_valid(form)
    
#======== Programa Auditoria =============
class ProgramaAuditoriaListView(ListView):
    model = ProgramaAuditoria
    template_name = 'auditorias/programa_list.html'
    context_object_name = 'programas'
    paginate_by = 10

    def get_queryset(self):
        return ProgramaAuditoria.objects.all().order_by('-ano')
    
class ProgramaAuditoriaDetailView(DetailView):
    model = ProgramaAuditoria
    template_name = 'auditorias/programa_detail.html'
    context_object_name = 'programa'

class ProgramaAuditoriaCreateView(CreateView):
    model = ProgramaAuditoria
    form_class = ProgramaAuditoriaForm
    template_name = 'auditorias/programa_form.html'
    success_url = reverse_lazy( 'auditorias:programa-list')

    def form_valid(self, form):
        messages.success(self.request, 'Programa de Auditoria criado com sucesso!')
        return super().form_valid(form)
    
class ProgramaAuditoriaUpdateView(UpdateView):
    model = ProgramaAuditoria
    form_class = ProgramaAuditoriaForm
    template_name = 'auditorias/programa_form.html'

    def get_success_url(self):
        return reverse_lazy('auditorias:programa-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Programa de Auditoria atualizado com sucesso!')
        return super().form_valid(form)
    
class ProgramaAuditoriaDeleteView(DetailView):
    model = ProgramaAuditoria
    template_name = 'auditoria/programa_confirm_delete.html'
    success_url = reverse_lazy('auditoria:programa-list')

    def delete(self, request,*args, **kwargs):
        messages.success(self.request, 'Programa de Auditoria excluído com sucesso!')
        return super().delete(request, *args, **kwargs)
    
# ======= Views para Histórico =======
class HistoricoAuditoriaView(LoginRequiredMixin, DetailView):
    model = Auditoria
    template_name = 'auditorias/historico_auditoria.html'
    context_object_name = 'auditoria'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtém todo o histórico ordenado por data (mais recente primeiro)
        context['historico'] = self.object.history.all().order_by('-history_date')
        return context

class HistoricoProgramaView(DetailView):
    model = ProgramaAuditoria
    template_name = 'auditorias/historico_programa.html'
    context_object_name = 'programa'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historico']