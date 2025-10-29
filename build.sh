#!/bin/bash
# build.sh

# Instala dependências
pip install -r requirements.txt

# Executa migrações
python manage.py migrate

# Coleta arquivos estáticos (se necessário)
python manage.py collectstatic --noinput