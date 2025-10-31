from django.urls import path
from . import views

app_name = 'help_sgi'

urlpatterns = [
    path('', views.help_home, name='help-home'),
]