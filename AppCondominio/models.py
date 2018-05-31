from django.db import models
from django.forms import ModelForm
# -*- encoding: iso-8859-1 -*-
# -*- encoding: utf-8 -*-
# Create your models here.


class Proprietario(models.Model):
	nome=models.CharField(max_length=50,default="")
	telefone=models.CharField(max_length=30,default="")
	pass

	def __str__(self):
		return self.nome

class Apartamento(models.Model):
	numero=models.IntegerField(null=False)
	qtdQuartos=models.IntegerField(null=False)
	proprietario=models.ForeignKey(Proprietario,on_delete=models.CASCADE,default=False)
	#isVazio=models.BooleanField(default=False)

	'''def __init__(self,num,qtd):
		self.numero=num
		self.qtdQuartos=qtd
	pass'''

class TipoDespesa(models.Model):
	nome=models.CharField(max_length=30,default="")
	valorRateado=models.BooleanField(default=False)
	
	def __str__(self):
		return self.nome

class Despesa(models.Model):
	mesAno=models.TextField(max_length=30,default="")
	valor=models.IntegerField(null=False)
	tipoDespesa=models.ForeignKey(TipoDespesa,on_delete=models.CASCADE,default=False)
	pass

class ItemCondominio(models.Model):
	referencia=models.TextField(max_length=30,default="")
	valor=models.IntegerField(null=False)
	despesa=models.ForeignKey(Despesa,on_delete=models.CASCADE,default=False)
	pass

class Condominio(models.Model):
	mesAno=models.TextField(max_length=30,default="")
	dataPagamento=models.DateField(auto_now=False)
	valorPago=models.IntegerField(null=False)
	valorPagar=models.IntegerField(null=False)
	apartamento=models.ForeignKey(Apartamento,on_delete=models.CASCADE,default=False)
	itens=models.ManyToManyField(ItemCondominio,default=False)
	pass