from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from banco.models import Conta, Movimentacao
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from banco.forms import SignUpForm, SignInForm, UserDataForm

# Create your views here.

@login_required
def home(request):
    conta = Conta.objects.get(usuario=request.user)
    context = {'conta': conta}
    return render(request, "inicio.html", context=context)

@login_required
def deposit(request):

    if request.method == 'GET':
        conta = Conta.objects.get(usuario=request.user)
        context = {'conta': conta}
        return render(request, "deposito.html", context=context)
    elif request.method == 'POST':
        montante = float(request.POST['montante'])
        conta = Conta.objects.get(usuario=request.user)
        res = conta.depositar(montante)
        if res:
            messages.success(request, "Dinheiro depositado!")
            return HttpResponseRedirect('/inicio/')
        else:
            messages.warning(request, "Digite um valor superior a zero!")
            return HttpResponseRedirect('/deposito/')

@login_required
def withdraw(request):

    if request.method == 'GET':
        conta = Conta.objects.get(usuario=request.user)
        context = {'conta': conta}
        return render(request, "levantamento.html", context=context)
    elif request.method == 'POST':
        montante = float(request.POST['montante'])
        conta = Conta.objects.get(usuario=request.user)
        res = conta.levantar(montante)
        if res:
            messages.success(request, "Dinheiro levantado!")
            return HttpResponseRedirect('/inicio/')
        else:
            messages.warning(
                request, "Não digite zero, um valor negativo ou superior ao que tem na conta!")
            return HttpResponseRedirect('/levantamento/')

@login_required
def profile(request):
    if request.method == 'GET':

        usuario = request.user

        form = UserDataForm(initial={
                            'primeiro_nome': usuario.perfil.primeiro_nome,
                            'ultimo_nome': usuario.perfil.ultimo_nome,
                            'telefone': usuario.perfil.telefone,
                            'morada': usuario.perfil.morada,
                            }, request=request)

        context = {'usuario': usuario, 'form': form, 'feedback': ''}

        return render(request, "dadoscliente.html", context=context)

    elif request.method == 'POST':

        form = UserDataForm(request.POST, request=request)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Dados atualizados!")
                return HttpResponseRedirect('/perfil/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect('/perfil/')
        else:
            context = {'form': form, 'feedback': 'd-block'}
            return render(request, 'dadoscliente.html', context=context)

@login_required
def transaction_history(request):
    conta = Conta.objects.get(usuario=request.user)
    movimentacoes = Movimentacao.objects.filter(conta=conta)
    context = {'conta': conta, 'movimentacoes': movimentacoes}
    return render(request, "movimentacoes.html", context=context)

def signIn(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')

    if request.method == 'GET':
        form = SignInForm(None)
        return render(request, 'entrar-registar/entrar.html', context={'form': form, 'feedback': ''})
    elif request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            return form.singIn(request=request)
        else:
            return render(request, 'entrar-registar/entrar.html', context={'form': form, 'feedback': 'd-block'})

def signUp(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')

    if request.method == 'GET':
        form = SignUpForm(None)
        return render(request, 'entrar-registar/registar.html', context={'form': form, 'feedback': ''})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, "Sua conta foi criada, faça o login!")
                return HttpResponseRedirect('/entrar/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect('/registar/')
        else:
            return render(request, 'entrar-registar/registar.html', context={'form': form, 'feedback': 'd-block'})

@login_required
def delete_account(request):
    if request.method == 'POST':
        btn = request.POST['eliminar_conta']
        if btn:
            usuario = request.user
            logout(request)
            usuario.delete()
            messages.success(request, "Conta deletada!")
            return HttpResponseRedirect('/entrar/')

@login_required
def my_logout(request):
    logout(request)
    messages.success(request, "Deslogado!")
    return HttpResponseRedirect('/')
