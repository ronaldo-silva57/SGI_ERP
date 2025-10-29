from django.urls import path
from . import views

app_name = 'meio_ambiente'

urlpatterns = [
    # Dashboard
    path('', views.meio_ambiente_dashboard, name='dashboard'),
    
    # Aspectos e Impactos
    path('aspectos/', views.AspectoImpactoListView.as_view(), name='aspecto-list'),
    path('aspectos/novo/', views.AspectoImpactoCreateView.as_view(), name='aspecto-create'),
    path('aspectos/<int:pk>/', views.AspectoImpactoDetailView.as_view(), name='aspecto-detail'),
    path('aspectos/<int:pk>/editar/', views.AspectoImpactoUpdateView.as_view(), name='aspecto-update'),
    
    # Licenças
    path('licencas/', views.LicencaAmbientalListView.as_view(), name='licenca-list'),
    path('licencas/novo/', views.LicencaAmbientalCreateView.as_view(), name='licenca-create'),
    path('licencas/<int:pk>/editar/', views.LicencaAmbientalUpdateView.as_view(), name='licenca-update'),
    
    # Emergências
    path('emergencias/', views.EmergenciaAmbientalListView.as_view(), name='emergencia-list'),
    path('emergencias/novo/', views.EmergenciaAmbientalCreateView.as_view(), name='emergencia-create'),
    path('emergencias/<int:pk>/', views.EmergenciaAmbientalDetailView.as_view(), name='emergencia-detail'),
    path('emergencias/<int:pk>/editar/', views.EmergenciaAmbientalUpdateView.as_view(), name='emergencia-update'),
]