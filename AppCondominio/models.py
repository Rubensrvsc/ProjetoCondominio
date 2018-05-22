from django.db import models
from django.forms import ModelForm

# Create your models here.


class Proprietario(models.Model):
	nome=models.CharField(max_length=50)
	telefone=models.CharField(max_length=30)
	pass

	def __str__(self):
		return self.nome

class Apartamento(models.Model):
	numero=models.IntegerField(null=False)
	qtdQuartos=models.IntegerField(null=False)
	propri=models.ForeignKey(Proprietario,on_delete=models.CASCADE)
	#isVazio=models.BooleanField()

	'''def __init__(self,num,qtd):
		self.numero=num
		self.qtdQuartos=qtd
	pass'''

'''class Condominio(models.Model):
	mesAno=models.TextField()
	#dataPagamento=DateField(null=False)
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
	nome=models.TextField()
	valorRateado=models.BooleanField()
	pass
'''