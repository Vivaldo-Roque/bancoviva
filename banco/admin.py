from django.contrib import admin
from .models import Conta, Movimentacao, Operacao, Perfil

# Registar aqui as classes

admin.site.register(Conta)
admin.site.register(Movimentacao)
admin.site.register(Operacao)
admin.site.register(Perfil)