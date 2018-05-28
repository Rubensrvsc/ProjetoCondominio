from django.db import models
from django.forms import ModelForm

# Create your models here.


class Apartamento(models.Model):
	numero=models.IntegerField()
	qtdQuartos=models.IntegerField()
	#isVazio=models.BooleanField()

	'''def __init__(self,num,qtd):
		self.numero=num
		self.qtdQuartos=qtd
	pass'''

'''class Proprietario(models.Model):
	nome=models.TextField()
	string=models.TextField()
	pass

class Condominio(models.Model):
	mesAno=models.TextField()
	#dataPagamento=DateField(null=True)
	valorPago=models.IntegerField()
	valorPagar=models.IntegerField()
	pass

class ItemCondominio(models.Model):
	referencia=models.TextField()
	valor=models.IntegerField()
	pass

class Despesa(models.Model):
	mesAno=models.TextField()
	valor=models.IntegerField()
	pass

class TipoDespesa(models.Model):
	nome=models.TextField()
	valorRateado=models.BooleanField()
	pass'''