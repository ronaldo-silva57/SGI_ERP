from django.urls import path
from . import views

app_name = 'gestao_documental'

urlpatterns = [
    #========= Documentos =========
    path('', views.DocumentoListView.as_view(), name='documento-list'),
    path('novo/', views.DocumentoCreateView.as_view(), name='documento-create'),
    path('<int:pk>/', views.DocumentoDetailView.as_view(), name='documento-detail'),
    path('<int:pk>/editar/', views.DocumentoUpdateView.as_view(), name='documento-update'),
    
    #========= Categorias ========
    path('categorias/', views.CategoriaDocumentoListView.as_view(), name='categoria-list'),
    path('categorias/nova/', views.CategoriaDocumentoCreateView.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/editar/', views.CategoriaDocumentoUpdateView.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/excluir/', views.CategoriaDocumentoDeleteView.as_view(), name='categoria-delete'),
    
    #========= Dashboard e AJAX =========
    path('dashboard/', views.documento_dashboard, name='documento-dashboard'),
    path('api/categoria/<int:categoria_id>/documentos/', views.get_categoria_documentos, name='categoria-documentos'),

    #========= Exportar xls e pdf =========
    path('documentos/exportar/pdf/', views.exportar_documentos_pdf, name='documento-export-pdf'),
    path('documentos/exportar/excel/', views.exportar_documentos_excel, name='documento-export-excel'),
]