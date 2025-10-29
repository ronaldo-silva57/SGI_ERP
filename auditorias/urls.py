from django.urls import path
from . import views

app_name = 'auditorias'

urlpatterns = [
    path('', views.AuditoriaListView.as_view(), name='auditoria-list'),
    path('novo/', views.AuditoriaCreateView.as_view(), name='auditoria-create'),
    path('<int:pk>/', views.AuditoriaDetailView.as_view(), name='auditoria-detail'),
    path('<int:pk>/editar/', views.AuditoriaUpdateView.as_view(), name='auditoria-update'),
]