from .models import Apartamento,Proprietario,Condominio
from django import forms


class apartamentoForm(forms.ModelForm):
	class Meta:
		model=Apartamento
		fields = '__all__' 

class proprietarioForm(forms.ModelForm):
	class Meta:
		model=Proprietario
		fields='__all__'

class condominioForm(forms.ModelForm):
	class Meta:
		model=Condominio
		fields='__all__'