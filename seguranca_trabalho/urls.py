from django.urls import path
from . import views

app_name = 'seguranca'

urlpatterns = [
    # Dashboard
    path('', views.seguranca_trabalho_dashboard, name='dashboard'),
    
    # Perigos e Riscos
    path('perigos/', views.PerigoRiscoListView.as_view(), name='perigo-list'),
    path('perigos/novo/', views.PerigoRiscoCreateView.as_view(), name='perigo-create'),
    path('perigos/<int:pk>/', views.PerigoRiscoDetailView.as_view(), name='perigo-detail'),
    path('perigos/<int:pk>/editar/', views.PerigoRiscoUpdateView.as_view(), name='perigo-update'),
    
    # Acidentes
    path('acidentes/', views.AcidenteListView.as_view(), name='acidente-list'),
    path('acidentes/novo/', views.AcidenteCreateView.as_view(), name='acidente-create'),
    path('acidentes/<int:pk>/', views.AcidenteDetailView.as_view(), name='acidente-detail'),
    path('acidentes/<int:pk>/editar/', views.AcidenteUpdateView.as_view(), name='acidente-update'),
    
    # Treinamentos
    path('treinamentos/', views.TreinamentoSSTListView.as_view(), name='treinamento-list'),
    path('treinamentos/novo/', views.TreinamentoSSTCreateView.as_view(), name='treinamento-create'),
    path('treinamentos/<int:pk>/', views.TreinamentoSSTDetailView.as_view(), name='treinamento-detail'),
    path('treinamentos/<int:pk>/editar/', views.TreinamentoSSTUpdateView.as_view(), name='treinamento-update'),
]