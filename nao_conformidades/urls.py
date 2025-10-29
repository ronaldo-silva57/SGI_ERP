from django.urls import path
from . import views

app_name = 'nao_conformidades'

urlpatterns = [
    path('', views.NaoConformidadeListView.as_view(), name='nao-conformidade-list'),
    path('dashboard/', views.nc_dashboard, name='nc-dashboard'),
    path('novo/', views.NaoConformidadeCreateView.as_view(), name='nao-conformidade-create'),
    path('<int:pk>/', views.NaoConformidadeDetailView.as_view(), name='nao-conformidade-detail'),
    path('<int:pk>/editar/', views.NaoConformidadeUpdateView.as_view(), name='nao-conformidade-update'),
]