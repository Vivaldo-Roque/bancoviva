from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, models.CASCADE, primary_key=True)
    primeiro_nome = models.CharField(max_length=50, blank=False)
    ultimo_nome = models.CharField(max_length=50, blank=False)
    telefone = models.CharField(max_length=50, blank=False)
    morada = models.CharField(max_length=50, blank=False)

    class Meta:
        managed = True
        db_table = 'perfis'
        verbose_name_plural = 'Perfis'

class Conta(models.Model):
    conta_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, models.CASCADE)
    saldo = models.FloatField(default=0)

    class Meta:
        managed = True
        db_table = 'contas'
        verbose_name_plural = 'Contas'

    def depositar(self, valor: float):
        if valor > 0.0:
            self.saldo += valor
            self.save()
            operacao = Operacao.objects.get(operacao_id=1)
            movimentacao = Movimentacao.objects.create(conta=self, montante=valor, operacao=operacao)
            movimentacao.save()
            return True
        else:
            return False
    
    def levantar(self, valor: float):
        if self.saldo >= valor and valor > 0:
            self.saldo -= valor
            self.save()
            operacao = Operacao.objects.get(operacao_id=2)
            movimentacao = Movimentacao.objects.create(conta=self, montante=valor, operacao=operacao)
            movimentacao.save()
            return True
        else:
            return False

class Operacao(models.Model):
    operacao_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30)

    def __str__(self) -> str:
        return "{} | {}".format(self.operacao_id, self.descricao)

    class Meta:
        managed = True
        db_table = 'operacoes'
        verbose_name_plural = 'Operacoes'

class Movimentacao(models.Model):
    movimentacao_id = models.AutoField(primary_key=True)
    conta = models.ForeignKey('Conta', models.CASCADE)
    montante = models.FloatField(blank=False)
    operacao = models.ForeignKey('Operacao', models.CASCADE, blank=False)
    data_hora = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        managed = True
        db_table = 'movimentacoes'
        verbose_name_plural = 'Movimentacoes'