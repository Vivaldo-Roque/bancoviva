Estive estudando Django e achei bem legal, tentei fazer um sistema que engloba o CRUD (Create-Read-Update-Delete), é um sistema que simula uma conta bancária simples.

Pode testar aqui => https://bancoviva.vercel.app/

O que pude aprender:

* O que é Django, e como ele simplifica o desenvolvimento.

* Django faz uso da arquitetura MVT (Moddel-View-Template).

* A diferença entre um projeto e app no Django.

* Django traz uma ORM facilitando gerênciamento do banco de dados (criacão de tabelas, relações, CRUD, migrações,  etc).

* Django tem uma maneira interessante de se reaproveitar os templates em outros templates.

* Utilizar algumas tags e filtros dos templates.

* Django tem um mecanismo para ajudar a lidar com HTML Forms, permitindo fazer a validação, customizar os campos e o tipo de dados, salvar direitamente para o banco de dados, etc.

* Quanto a autenticação de usuário, Django traz um sistema de autenticação embutido.

* Django traz um mecânismo para definir rotas.

Para fazer o deploy do projeto na Vercel tive que seguir alguns passos:
* https://www.makeuseof.com/django-app-vercel-host-free/
* https://devmaesters.com/blog/15

instalação:

pip install -r requirements.txt

Comandos uteis:

criar novo projeto django
django-admin startproject myprojectname

criar um novo app para o projeto
py manage.py startapp myappname

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

Linha de comando interativa:
py manage.py shell