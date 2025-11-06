from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

def create_initial_superuser(request):
    """View temporária para criar superusuário - REMOVER APÓS USO"""
    User = get_user_model()
    
    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse('Superusuário já existe!')
    
    try:
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        return HttpResponse('Superusuário criado com sucesso!')
    except Exception as e:
        return HttpResponse(f'Erro: {str(e)}')

urlpatterns = [
    # ⚠️ TEMPORÁRIO - criar superusuário
    path('create-superuser/', create_initial_superuser, name='create_superuser'),
    
    path('admin/', admin.site.urls),
    
    # ✅ URLs de autenticação na raiz
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # ✅ Dashboard protegido
    #path('dashboard/', login_required(TemplateView.as_view(template_name='dashboard.html')), name='dashboard'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    
    # ✅ Redirecionamento da raiz para dashboard (ou login)
    #path('', login_required(TemplateView.as_view(template_name='dashboard.html')), name='home'),
    path('', TemplateView.as_view(template_name='dashboard.html'), name='home'),

    # Suas outras URLs
    path('usuarios/', include('usuarios.urls')),
    path('documentos/', include('gestao_documental.urls')),
    path('nao-conformidades/', include('nao_conformidades.urls')),
    path('auditorias/', include('auditorias.urls')),
    path('indicadores/', include('indicadores.urls')),
    path('analise-critica/', include('analise_critica.urls')),
    path('meio-ambiente/', include('meio_ambiente.urls')),
    path('seguranca-trabalho/', include('seguranca_trabalho.urls')),
    path('help-sgi/', include('help_sgi.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)