from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ApartamentoForm
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    return render(request,'teste_javascript.html')

def boot(request):
	return render(request,'teste_bootstrap.html')

def apartForm(request):
	form=ApartamentoForm()
	return render(request, 'formulario_teste.html',{'form':form})
