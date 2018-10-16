from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse
from configuracion.forms import *
from configuracion.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Create your views here.
def index(request):
	estudios = Estudio.objects.all().order_by('id')
	num_fisico = 0
	num_biologico = 0
	num_socio_cultural = 0
	for i in estudios:
		if i.tipo == "FS":
			num_fisico+=1
		elif i.tipo == "BIO":
			num_biologico+=1
		else:
			num_socio_cultural+=1
	num_filas = max((num_fisico, num_biologico, num_socio_cultural))
	print(num_filas)

	return render(request, 'configuracion/index.html', {'estudios':estudios, 'num_filas':num_filas})

# Formulario para registrar un estudio/impacto
class EstudioCreate(CreateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'
	success_url = reverse_lazy('index')

class EstudioUpdate(UpdateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'
	success_url = reverse_lazy('index')

class EstudioDelete(DeleteView):
	model = Estudio
	success_url = reverse_lazy('index')

