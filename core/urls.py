from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def create_initial_superuser(request):
    """View temporária para criar superusuário - REMOVER APÓS USO"""
    User = get_user_model()
    
    # Verificar se já existe algum superusuário
    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse('''
            <html>
            <body style="font-family: Arial, sans-serif; padding: 20px;">
                <h1>⚠️ Superusuário já existe!</h1>
                <p>Já existe um superusuário no sistema.</p>
                <div style="margin-top: 20px;">
                    <a href="/admin/" style="padding: 10px 15px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Ir para Admin</a>
                    <a href="/" style="padding: 10px 15px; background: #6c757d; color: white; text-decoration: none; border-radius: 5px; margin-left: 10px;">Página Inicial</a>
                </div>
            </body>
            </html>
        ''')
    
    # Criar superusuário
    try:
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        return HttpResponse('''
            <html>
            <body style="font-family: Arial, sans-serif; padding: 20px;">
                <h1 style="color: green;">✅ Superusuário Criado com Sucesso!</h1>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
                    <p><strong>Usuário:</strong> admin</p>
                    <p><strong>Senha:</strong> admin123</p>
                    <p><strong>Email:</strong> admin@example.com</p>
                </div>
                <div style="background: #fff3cd; padding: 15px; border-radius: 5px; margin: 15px 0; border: 1px solid #ffeaa7;">
                    <strong>⚠️ IMPORTANTE:</strong> Após fazer login, REMOVA esta rota do código!
                </div>
                <div style="margin-top: 20px;">
                    <a href="/admin/" style="padding: 12px 25px; background: #28a745; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">Ir para Login Admin</a>
                </div>
            </body>
            </html>
        ''')
    except Exception as e:
        return HttpResponse(f'''
            <html>
            <body style="font-family: Arial, sans-serif; padding: 20px;">
                <h1 style="color: red;">❌ Erro ao criar superusuário</h1>
                <p><strong>Erro:</strong> {str(e)}</p>
                <p>Verifique se as migrações foram aplicadas corretamente.</p>
                <a href="/" style="padding: 10px 15px; background: #6c757d; color: white; text-decoration: none; border-radius: 5px;">Voltar</a>
            </body>
            </html>
        ''')

urlpatterns = [
    # ⚠️ ADICIONE ESTA LINHA TEMPORARIAMENTE - PRIMEIRA POSIÇÃO ⚠️
    path('create-superuser/', create_initial_superuser, name='create_superuser'),
    
    # Suas URLs normais
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
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