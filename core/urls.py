from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
