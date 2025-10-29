from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    # URLs de autenticação do Django
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # URLs de gestão de usuários
    path('', views.UsuarioListView.as_view(), name='usuario-list'),
    path('novo/', views.UsuarioCreateView.as_view(), name='usuario-create'),
    path('<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('<int:pk>/editar/', views.UsuarioUpdateView.as_view(), name='usuario-update'),
]