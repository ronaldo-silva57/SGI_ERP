from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AspectoImpactoAmbiental, LicencaAmbiental, EmergenciaAmbiental
from .forms import AspectoImpactoAmbientalForm, LicencaAmbientalForm, EmergenciaAmbientalForm

# AspectoImpactoAmbiental Views
#class AspectoImpactoListView(LoginRequiredMixin, ListView):
class AspectoImpactoListView(ListView):
    model = AspectoImpactoAmbiental
    template_name = 'meio_ambiente/aspecto_list.html'
    context_object_name = 'aspectos'
    paginate_by = 10

#class AspectoImpactoDetailView(LoginRequiredMixin, DetailView):
class AspectoImpactoDetailView(DetailView):
    model = AspectoImpactoAmbiental
    template_name = 'meio_ambiente/aspecto_detail.html'
    context_object_name = 'aspecto'

#class AspectoImpactoCreateView(LoginRequiredMixin, CreateView):
class AspectoImpactoCreateView(CreateView):
    model = AspectoImpactoAmbiental
    form_class = AspectoImpactoAmbientalForm
    template_name = 'meio_ambiente/aspecto_form.html'
    success_url = reverse_lazy('meio-ambiente:aspecto-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Aspecto/Impacto ambiental registrado com sucesso!')
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['responsavel'] = self.request.user
        return initial

#class AspectoImpactoUpdateView(LoginRequiredMixin, UpdateView):
class AspectoImpactoUpdateView(UpdateView):
    model = AspectoImpactoAmbiental
    form_class = AspectoImpactoAmbientalForm
    template_name = 'meio_ambiente/aspecto_form.html'
    
    def get_success_url(self):
        return reverse_lazy('meio-ambiente:aspecto-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Aspecto/Impacto ambiental atualizado com sucesso!')
        return super().form_valid(form)

# LicencaAmbiental Views
#class LicencaAmbientalListView(ListView):
class LicencaAmbientalListView(LoginRequiredMixin, ListView):
    model = LicencaAmbiental
    template_name = 'meio_ambiente/licenca_list.html'
    context_object_name = 'licencas'
    paginate_by = 10

#class LicencaAmbientalCreateView(CreateView):
class LicencaAmbientalCreateView(LoginRequiredMixin, CreateView):
    model = LicencaAmbiental
    form_class = LicencaAmbientalForm
    template_name = 'meio_ambiente/licenca_form.html'
    success_url = reverse_lazy('meio-ambiente:licenca-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Licença ambiental cadastrada com sucesso!')
        return super().form_valid(form)

#class LicencaAmbientalUpdateView(LoginRequiredMixin, UpdateView):
class LicencaAmbientalUpdateView(UpdateView):
    model = LicencaAmbiental
    form_class = LicencaAmbientalForm
    template_name = 'meio_ambiente/licenca_form.html'
    success_url = reverse_lazy('meio-ambiente:licenca-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Licença ambiental atualizada com sucesso!')
        return super().form_valid(form)

# EmergenciaAmbiental Views
#class EmergenciaAmbientalListView(LoginRequiredMixin, ListView):
class EmergenciaAmbientalListView(ListView):
    model = EmergenciaAmbiental
    template_name = 'meio_ambiente/emergencia_list.html'
    context_object_name = 'emergencias'
    paginate_by = 10

#class EmergenciaAmbientalCreateView(LoginRequiredMixin, CreateView):
class EmergenciaAmbientalCreateView(CreateView):
    model = EmergenciaAmbiental
    form_class = EmergenciaAmbientalForm
    template_name = 'meio_ambiente/emergencia_form.html'
    success_url = reverse_lazy('meio-ambiente:emergencia-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Emergência ambiental registrada com sucesso!')
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['responsavel'] = self.request.user
        return initial

#class EmergenciaAmbientalUpdateView(LoginRequiredMixin, UpdateView):
class EmergenciaAmbientalUpdateView(UpdateView):
    model = EmergenciaAmbiental
    form_class = EmergenciaAmbientalForm
    template_name = 'meio_ambiente/emergencia_form.html'
    
    def get_success_url(self):
        return reverse_lazy('meio-ambiente:emergencia-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Emergência ambiental atualizada com sucesso!')
        return super().form_valid(form)

class EmergenciaAmbientalDetailView(DetailView):
    model = EmergenciaAmbiental
    template_name = 'meio_ambiente/emergencia_detail.html'


# Dashboard
def meio_ambiente_dashboard(request):
    aspectos_count = AspectoImpactoAmbiental.objects.count()
    aspectos_criticos = AspectoImpactoAmbiental.objects.filter(nivel_significancia='critico').count()
    licencas_count = LicencaAmbiental.objects.count()
    emergencias_count = EmergenciaAmbiental.objects.count()
    
    context = {
        'aspectos_count': aspectos_count,
        'aspectos_criticos': aspectos_criticos,
        'licencas_count': licencas_count,
        'emergencias_count': emergencias_count,
    }
    return render(request, 'meio_ambiente/dashboard.html', context)