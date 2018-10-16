from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse
from configuracion.forms import *
from configuracion.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Create your views here.
def index(request):
	estudios = Estudio.objects.all().order_by('id')
	return render(request, 'configuracion/index.html', {'estudios':estudios})

# # Create your views here.
# def agregar_estudio(request):
# 	return render(request, 'configuracion/agregar_estudio.html', {})

# Formulario para registrar un estudio/impacto
class EstudioCreate(CreateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'
	success_url = reverse_lazy('index')