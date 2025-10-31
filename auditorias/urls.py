from django.urls import path
from . import views

app_name = 'auditorias'

urlpatterns = [

    #======== Auditoria =========
    path('', views.AuditoriaListView.as_view(), name='auditoria-list'),
    path('novo/', views.AuditoriaCreateView.as_view(), name='auditoria-create'),
    path('<int:pk>/', views.AuditoriaDetailView.as_view(), name='auditoria-detail'),
    path('<int:pk>/editar/', views.AuditoriaUpdateView.as_view(), name='auditoria-update'),

    #========= Programa Auditoria ========
    path('programas/', views.ProgramaAuditoriaListView.as_view(), name='programa-list'),
    path('programas/novo/', views.ProgramaAuditoriaCreateView.as_view(), name='programa-create'),
    path('programas/<int:pk>/', views.ProgramaAuditoriaDetailView.as_view(), name='programa-detail'),
    path('programas/<int:pk>/editar/', views.ProgramaAuditoriaUpdateView.as_view(), name='programa-update'),
    path('programas/<int:pk>/excluir/', views.ProgramaAuditoriaDeleteView.as_view(), name='programa-delete'),

    #======== History ========
    path('<int:pk>/historico/', views.HistoricoAuditoriaView.as_view(), name='auditoria-historico'),
    path('programas/<int:pk>/historico/', views.HistoricoProgramaView.as_view(), name='programa-historico'),
]