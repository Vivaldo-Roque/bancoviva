from django.urls import path
from banco import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('inicio/', views.home, name='inicio'),
    path('entrar/', views.signIn, name='entrar'),
    path('registar/', views.signUp, name='registar'),
    path('sair/', views.my_logout, name='sair'),
    path('eliminar_conta/', views.delete_account, name='eliminar_conta'),
    path('deposito/', views.deposit, name='deposito'),
    path('levantamento/', views.withdraw, name='levantamento'),
    path('perfil/', views.profile, name='perfil'),
    path('historico_movimentacoes/', views.transaction_history, name='historico_movimentacoes')
]