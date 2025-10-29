from django.urls import path
from . import views

app_name = 'indicadores'

urlpatterns = [
    path('', views.IndicadorListView.as_view(), name='indicador-list'),
    path('novo/', views.IndicadorCreateView.as_view(), name='indicador-create'),
    path('<int:pk>/', views.IndicadorDetailView.as_view(), name='indicador-detail'),
    path('<int:pk>/editar/', views.IndicadorUpdateView.as_view(), name='indicador-update'),

    path('exportar/pdf/', views.exportar_indicadores_pdf, name='exportar-pdf'),
    path('exportar/excel/', views.exportar_indicadores_excel, name='exportar-excel'),
]
