from django.urls import path
from . import views

app_name = 'gestao_documental'

urlpatterns = [
    path('', views.DocumentoListView.as_view(), name='documento-list'),
    path('novo/', views.DocumentoCreateView.as_view(), name='documento-create'),
    path('<int:pk>/', views.DocumentoDetailView.as_view(), name='documento-detail'),
    path('<int:pk>/editar/', views.DocumentoUpdateView.as_view(), name='documento-update'),
]
