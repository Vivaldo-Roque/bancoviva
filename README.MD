Google pesquisar sobre Django e Arquitectura MVT

Instalar Django

pip install django

criar novo projeto django:
django-admin startproject project_banksimulator

criar um novo app para o projeto:
py manage.py startapp app_banksimulator

Criar modelos de uma base de dados já existente:
py manage.py inspectdb > models.py
py manage.py makemigrations myappname
py manage.py migrate myappname --fake-initial

Criar usuario adminstrador
py manage.py createsuperuser

Resetar migrações
manage.py migrate --fake myappname zero

criar migração
python manage.py makemigrations myappname --name mymigrationname --empty
py manage.py makemigrations myappname
py manage.py migrate

Iniciar o projeto
py manage.py runserver