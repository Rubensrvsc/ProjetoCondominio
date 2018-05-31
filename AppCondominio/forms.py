from .models import Apartamento,Proprietario,Condominio,ItemCondominio,Despesa,TipoDespesa
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

class itemForm(forms.ModelForm):
	class Meta:
		model=ItemCondominio
		fields='__all__'

class despesaForm(forms.ModelForm):
	class Meta:
		model=Despesa
		fields='__all__'

class tipoDespesaForm(forms.ModelForm):
	class Meta:
		model=TipoDespesa
		fields='__all__'
			