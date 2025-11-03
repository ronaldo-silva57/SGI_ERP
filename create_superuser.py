import os
import django
import sys

# Adiciona o diretório do projeto ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    
    if User.objects.filter(username='admin').exists():
        print("ℹ️ Superusuário já existe.")
        return
    
    try:
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com', 
            password='senha123'
        )
        print("✅ Superusuário criado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar superusuário: {str(e)}")

if __name__ == "__main__":
    create_superuser()