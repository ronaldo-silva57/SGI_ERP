from django.urls import path
from . import views

app_name = 'analise_critica'

urlpatterns = [
    path('', views.AnaliseCriticaListView.as_view(), name='analise-critica-list'),
    path('dashboard/', views.analise_critica_dashboard, name='analise-critica-dashboard'),
    path('novo/', views.AnaliseCriticaCreateView.as_view(), name='analise-critica-create'),
    path('<int:pk>/', views.AnaliseCriticaDetailView.as_view(), name='analise-critica-detail'),
    path('<int:pk>/editar/', views.AnaliseCriticaUpdateView.as_view(), name='analise-critica-update'),
]
