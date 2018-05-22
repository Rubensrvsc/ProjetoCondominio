from .models import Apartamento
from django import forms


class ApartamentoForm(forms.ModelForm):
	class Meta:
		model=Apartamento
		fields = '__all__' 