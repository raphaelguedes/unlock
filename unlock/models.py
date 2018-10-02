from django.db import models
from django.utils import timezone

from django.conf import settings
from django.contrib.auth.models import User

from django.db import models
import datetime


class Setor(models.Model):
	nome_setor = models.CharField(max_length=30)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

	def __str__(self):
		return self.nome_setor

class Pessoas(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
	nome_pessoa = models.CharField(max_length=100)
	email = models.CharField(max_length=200, null=True)
	setor_pessoa = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True)
	codigo_cartao = models.CharField(max_length=30)
	cpf = models.CharField(max_length=15)
	
	def __str__(self):
		return self.nome_pessoa


class Porta(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
	numero_porta = models.IntegerField(default=0)
	setor_porta = models.ForeignKey(Setor, on_delete=models.CASCADE,null=True)
	descricao_porta = models.CharField(max_length=200)
	codigo_porta = models.CharField(max_length=10)
	ip = models.CharField(max_length=30)

	def __str__(self):
		return str(self.numero_porta)

class Acesso(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
	pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
	porta = models.ForeignKey(Porta, on_delete=models.CASCADE)
	permissao_acesso =  models.BooleanField(default=True)
	def __str__(self):
		return str(self.id)

class Registro(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
	acesso = models.ForeignKey(Acesso, on_delete=models.CASCADE, null=True)
	data_acesso = models.DateTimeField(default=timezone.now)
	pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, null=True)
	porta_acessada = models.ForeignKey(Porta, on_delete=models.CASCADE, null=True)
	codigo_recebido = models.CharField(max_length=30)
	permissao =  models.BooleanField(default=False)

	def __str__(self):
		return str(self.data_acesso.strftime("%d %m %Y-%H:%M:%S"))

class Status(models.Model):
	nome_status = models.CharField(max_length=40)
	def __str__(self):
		return str(self.nome_status)

class Botao(models.Model):
	nome_botao = models.CharField(max_length=100)
	endereco_botao = models.CharField(max_length=300)
	cep = models.CharField(max_length=9)
	email_botao = models.CharField(max_length=200, null=True)
	telefone_botao = models.CharField(max_length=15, null=True)
	situacao = models.ForeignKey(Status, on_delete=models.CASCADE,default = 1)
	key_botao = models.CharField(max_length=10)
	def __str__(self):
		return str(self.nome_botao)

class Registrobotao(models.Model):
	data_acesso = models.DateTimeField(default=timezone.now)
	nome_botao = models.ForeignKey(Botao, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.data_acesso.strftime("%d %m %Y-%H:%M:%S"))

