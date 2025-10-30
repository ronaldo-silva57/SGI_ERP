from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UsuarioCustomizado
from .forms import UsuarioCustomizadoCreationForm, UsuarioCustomizadoChangeForm

#class UsuarioListView(LoginRequiredMixin, ListView):
class UsuarioListView(ListView):
    model = UsuarioCustomizado
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'
    paginate_by = 15
    
    def get_queryset(self):
        return UsuarioCustomizado.objects.all().order_by('first_name', 'last_name')

#class UsuarioCreateView(LoginRequiredMixin, CreateView):
class UsuarioCreateView(CreateView):
    model = UsuarioCustomizado
    form_class = UsuarioCustomizadoCreationForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Usuário criado com sucesso!')
        return super().form_valid(form)

#class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
class UsuarioUpdateView(UpdateView):
    model = UsuarioCustomizado
    form_class = UsuarioCustomizadoChangeForm
    template_name = 'usuarios/usuario_form.html'
    
    def get_success_url(self):
        return reverse_lazy('usuario-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Usuário atualizado com sucesso!')
        return super().form_valid(form)

#class UsuarioDetailView(LoginRequiredMixin, DetailView):
class UsuarioDetailView(DetailView):
    model = UsuarioCustomizado
    template_name = 'usuarios/usuario_detail.html'
    context_object_name = 'usuario'