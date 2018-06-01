from django.shortcuts import render
from django.http import HttpResponse
from .models import Apartamento,Proprietario
from .forms import apartamentoForm,proprietarioForm,condominioForm,itemForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
# Create your views here.

def apartForm(request):
	form=apartamentoForm(request.POST or None)
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('inicio')
		else:
			form=apartamentoForm()
	return render(request, 'formulario_apartamento.html',{'form':form})

def proprietarioFormulario(request):
	formProprietario=proprietarioForm(request.POST or None)
	if request.method=='POST':
		if formProprietario.is_valid():
			formProprietario.save()
			return redirect('inicio')
		else:
			formProprietario=proprietarioForm()
	return render(request,'formulario_proprietario.html',{'formProprietario':formProprietario})

def condominioFormulario(request):
	formCondominio=condominioForm(request.POST)
	if request=='POST':
		if formCondominio.is_valid():
			formCondominio.save()
			return redirect('inicio')
		else:
			formCondominio=condominioForm()
	return render(request,'formulario_condominio.html',{'formCondominio':formCondominio})

def inicio(request):
	return render(request,'tela_inicial.html')

def obtemApartamentos(request):
	ver_apartamentos=Apartamento.objects.all()
	return render(request,'ver_apartamentos.html',{'apartamento':ver_apartamentos})
	pass

def itemCondominio(request):
	formItem=itemForm(request.POST or None)
	if request=='POST':
		if formItem.is_valid():
			formItem.save()
			return redirect('inicio')
		else:
			formItem=itemForm()
	return render(request,'formulario_item.html',{'formItem':formItem})