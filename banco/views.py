from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from banco.models import Perfil, Conta, Movimentacao
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create your views here.

@login_required  
def home(request):
    conta = Conta.objects.get(usuario=request.user)
    context = { 'conta': conta }
    return render(request, "inicio.html", context=context)

@login_required    
def deposit(request):

    if request.method == 'GET':
        conta = Conta.objects.get(usuario=request.user)
        context = { 'conta': conta }
        return render(request, "deposito.html", context=context)
    elif request.method == 'POST':
        montante = float(request.POST['montante'])
        conta = Conta.objects.get(usuario=request.user)
        res = conta.depositar(montante)
        if res:
            messages.success(request, "Dinheiro depositado!" )
            return HttpResponseRedirect('/inicio/')
        else:
            messages.warning(request, "Digite um valor superior a zero!" )
            return HttpResponseRedirect('/deposito/')

@login_required   
def withdraw(request):

    if request.method == 'GET':
        conta = Conta.objects.get(usuario=request.user)
        context = { 'conta': conta }
        return render(request, "levantamento.html", context=context)
    elif request.method == 'POST':
        montante = float(request.POST['montante'])
        conta = Conta.objects.get(usuario=request.user)
        res = conta.levantar(montante)
        if res:
            messages.success(request, "Dinheiro levantado!" )
            return HttpResponseRedirect('/inicio/')
        else:
            messages.warning(request, "Não digite um valor superior ao que tem na conta!" )
            return HttpResponseRedirect('/levantamento/')
    
@login_required  
def profile(request):
    if request.method == 'GET':
        usuario = request.user
        context = { 'usuario': usuario }
        return render(request, "dadoscliente.html", context=context)
    elif request.method == 'POST':
        primeiro_nome = request.POST['primeiro_nome']
        ultimo_nome = request.POST['ultimo_nome']
        telefone = request.POST['telefone']
        morada = request.POST['morada']
        senha = request.POST['senha']
        confirmar_senha = request.POST['csenha']

        if senha == '' and confirmar_senha == '':
            usuario = request.user
            perfil = Perfil(usuario=usuario, primeiro_nome=primeiro_nome, ultimo_nome=ultimo_nome, telefone=telefone, morada=morada)
            perfil.save()
            messages.success(request, "Dados atualizados!" )
            return HttpResponseRedirect('/perfil/')
        else:
            if senha == confirmar_senha:
                usuario = request.user
                perfil = Perfil(usuario=usuario, primeiro_nome=primeiro_nome, ultimo_nome=ultimo_nome, telefone=telefone, morada=morada)
                perfil.save()
                usuario.set_password(senha)
                update_session_auth_hash(request, usuario)
                usuario.save()
                messages.success(request, "Dados atualizados!" )
                return HttpResponseRedirect('/perfil/')

@login_required    
def transaction_history(request):
    conta = Conta.objects.get(usuario=request.user)
    movimentacoes = Movimentacao.objects.filter(conta=conta)
    context = { 'conta': conta, 'movimentacoes': movimentacoes }
    return render(request, "movimentacoes.html", context=context)

def signin(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')

    if request.method == 'GET':
        return render(request, 'entrar-registar/entrar.html')
    elif request.method == 'POST':
        email = request.POST['email']
        try:
            usuario_aux = User.objects.get(email=email)

            if usuario_aux:
                usuario_aux = User.objects.get(email=email)
                password = request.POST["senha"]
                usuario = authenticate(username=usuario_aux.username,password=password)
                if usuario is not None:
                    login(request, usuario)
                    messages.success(request, "Logado!" )
                    return HttpResponseRedirect('/inicio/')
                else:
                    messages.error(request, "E-mail ou senha inválidos!" )
                    return HttpResponseRedirect('/entrar/')

        except User.DoesNotExist:
            messages.error(request, "E-mail ou senha inválidos!" )
            return HttpResponseRedirect('/entrar/')


def signup(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')

    if request.method == 'GET':
        return render(request, 'entrar-registar/registar.html')
    elif request.method == 'POST':
        email = request.POST['email']
        try:
            usuario_aux = User.objects.get(email=email)

            if usuario_aux:
                messages.error(request, "Já existe um usuário com o mesmo e-mai!" )
                return HttpResponseRedirect('/registar/')

        except User.DoesNotExist:
            primeiro_nome = request.POST['primeiro_nome']
            ultimo_nome = request.POST['ultimo_nome']
            telefone = request.POST['telefone']
            morada = request.POST['morada']
            email = request.POST['email']
            senha = request.POST['senha']
            confirmar_senha = request.POST['csenha']

            if senha == confirmar_senha:
                try:
                    novoUsuario = User.objects.create_user(username=email,email=email, password=senha)
                    novoPerfil = Perfil(primeiro_nome=primeiro_nome, ultimo_nome=ultimo_nome, telefone=telefone, morada=morada, usuario=novoUsuario)
                    novoPerfil.save()
                    novaConta = Conta(saldo=0, usuario=novoUsuario)
                    novaConta.save()
                    messages.success(request, "Sua conta foi criada, faça o login!" )
                except:
                    novoUsuario.delete()
                    messages.error(request, "Por favor tente novamente!" )
                    return HttpResponseRedirect('/registar/')
                return HttpResponseRedirect('/entrar/')
            else:
                messages.error(request, "As duas senhas digitadas não são iguais!" )
                return HttpResponseRedirect('/registar/')

@login_required
def delete_account(request):
    if request.method == 'POST':
        btn = request.POST['eliminar_conta']
        if btn:
            usuario = request.user
            logout(request)
            usuario.delete()
            messages.success(request, "Conta deletada!" )
            return HttpResponseRedirect('/entrar/')

@login_required
def my_logout(request):
    logout(request)
    messages.success(request, "Deslogado!" )
    return HttpResponseRedirect('/')