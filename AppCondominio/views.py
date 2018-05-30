from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import apartamentoForm,proprietarioForm,condominioForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request,'teste_javascript.html')

def boot(request):
	return render(request,'teste_bootstrap.html')

def apartForm(request):
	form=apartamentoForm(request.POST or None)
	if request.method=='POST':
		if form.is_valid():
			form.save()
		else:
			form=apartamentoForm()
	return render(request, 'formulario_teste.html',{'form':form})

def proprietarioFormulario(request):
	formProprietario=proprietarioForm(request.POST or None)
	if request.method=='POST':
		if formProprietario.is_valid():
			formProprietario.save()
		else:
			formProprietario=proprietarioForm()
	return render(request,'formulario_proprietario.html',{'formProprietario':formProprietario})

def condominioFormulario(request):
	formCondominio=condominioForm(request.POST or None)
	if request=='POST':
		if formCondominio.is_valid():
			formCondominio.save()
		else:
			formCondominio=condominioForm()
	return render(request,'formulario_condominio.html',{'formCondominio':formCondominio})

def inicio(request):
	return render(request,'tela_inicial.html')
