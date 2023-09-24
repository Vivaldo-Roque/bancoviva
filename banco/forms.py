from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from django.http import HttpResponseRedirect
from banco.models import Perfil, Conta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import re

# signup form


class SignUpForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ['usuario']

    primeiro_nome = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Primeiro nome',
        'id': 'floatingFirstName'
    }))

    ultimo_nome = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Primeiro nome',
        'id': 'floatingLastName'
    }))

    telefone = forms.CharField(required=False, max_length=50, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Número de telefone',
        'id': 'floatingPhone'
    }))

    morada = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Morada',
        'id': 'floatingAddress'
    }))

    email = forms.EmailField(required=False, max_length=100, widget=EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'exemplo@exemplo.com',
        'id': 'floatingEmail'
    }))

    password = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Senha',
        'id': 'floatingPassword',
        'type': 'password'
    }))

    confirm_password = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Confirmar senha',
        'id': 'floatingCPassword',
        'type': 'password'
    }))

    def clean(self):
        super(SignUpForm, self).clean()

        # getting email and password from cleaned_data
        primeiro_nome = self.cleaned_data.get('primeiro_nome')
        ultimo_nome = self.cleaned_data.get('ultimo_nome')
        telefone = self.cleaned_data.get('telefone')
        morada = self.cleaned_data.get('morada')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        # validating the email and password

        if primeiro_nome == "" or primeiro_nome.isspace():
            self._errors['primeiro_nome'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if ultimo_nome == "" or ultimo_nome.isspace():
            self._errors['ultimo_nome'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if morada == "" or morada.isspace():
            self._errors['morada'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if telefone == "" or telefone.isspace():
            self._errors['telefone'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if email == "" or email.isspace():
            self._errors['email'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if password == "" or password.isspace():
            self._errors['password'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if confirm_password == "" or confirm_password.isspace():
            self._errors['confirm_password'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if email:
            if User.objects.filter(email=email).exists():
                self._errors['email'] = self.error_class(
                    ['E-mail digitado já em uso!'])

        if password != confirm_password:
            self._errors['password'] = self.error_class(['Senha não igual!'])
            self._errors['confirm_password'] = self.error_class(
                ['Senha não igual!'])
            self.initial["password"] = ''

        return self.cleaned_data

    def save(self, commit=True):

        instance = super(SignUpForm, self).save(commit=False)

        # do you logic here
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        novoUsuario = User.objects.create_user(username=email, email=email, password=password)
        instance.usuario = novoUsuario

        if commit:
            # Saving your form
            instance.save()

        novaConta = Conta(saldo=0, usuario=novoUsuario)
        novaConta.save()
        
        return instance

class SignInForm(forms.Form):
    class Meta:
        model = User
        fields = ['email', 'password']

    email = forms.EmailField(required=False, max_length=100, widget=EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'exemplo@exemplo.com',
        'id': 'floatingEmail'
    }))

    password = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Senha',
        'id': 'floatingPassword',
        'type': 'password'
    }))

    def clean(self):
        super(SignInForm, self).clean()

        # getting email and password from cleaned_data
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # validating the email and password

        if email == "" or email.isspace():
            self._errors['email'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if password == "" or password.isspace():
            self._errors['password'] = self.error_class(
                ['Campo não pode estar vazio!'])

        return self.cleaned_data

    def singIn(self, request):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            usuario_aux = User.objects.get(email=email)
            password = self.cleaned_data['password']
            usuario = authenticate(request, username=usuario_aux.username, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, "Logado!")
                return HttpResponseRedirect('/inicio/')
            else:
                messages.error(request, "E-mail ou senha inválidos!")
                return HttpResponseRedirect('/entrar/')
        else:
            messages.error(request, "E-mail ou senha inválidos!")
            return HttpResponseRedirect('/entrar/')

class UserDataForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ['usuario']

    primeiro_nome = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Primeiro nome',
        'id': 'floatingFirstName'
    }))

    ultimo_nome = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Primeiro nome',
        'id': 'floatingLastName'
    }))

    telefone = forms.CharField(required=False, max_length=50, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Número de telefone',
        'id': 'floatingPhone'
    }))

    morada = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Morada',
        'id': 'floatingAddress'
    }))

    password = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Senha',
        'id': 'floatingPassword',
        'type': 'password'
    }))

    confirm_password = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Confirmar senha',
        'id': 'floatingCPassword',
        'type': 'password'
    }))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(UserDataForm, self).__init__(*args, **kwargs)
        self.usuario = self.request.user

    def clean(self):
        super(UserDataForm, self).clean()

        # getting email and password from cleaned_data
        primeiro_nome = self.cleaned_data.get('primeiro_nome')
        ultimo_nome = self.cleaned_data.get('ultimo_nome')
        telefone = self.cleaned_data.get('telefone')
        morada = self.cleaned_data.get('morada')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        # validating the email and password

        if primeiro_nome == "" or primeiro_nome.isspace():
            self._errors['primeiro_nome'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if ultimo_nome == "" or ultimo_nome.isspace():
            self._errors['ultimo_nome'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if morada == "" or morada.isspace():
            self._errors['morada'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if telefone == "" or telefone.isspace():
            self._errors['telefone'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if password != confirm_password:
            self._errors['password'] = self.error_class(['Senha não igual!'])
            self._errors['confirm_password'] = self.error_class(['Senha não igual!'])
            self.initial["password"] = ''

        return self.cleaned_data

    def save(self, commit=True):

        instance = super(UserDataForm, self).save(commit=False)

        # do you logic here

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != '' and confirm_password != '':
            self.usuario.set_password(password)
            update_session_auth_hash(self.request, self.usuario)
            self.usuario.save()

        instance.usuario = self.usuario

        if commit:
            # Saving your form
            instance.save()
        
        return instance
