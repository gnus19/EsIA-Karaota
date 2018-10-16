from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from configuracion.forms import *
from configuracion.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

#Create your views here.
def index(request):
	estudios_fisicos = Estudio.objects.filter(tipo="FS")
	estudios_biologicos = Estudio.objects.filter(tipo="BIO")
	estudios_socioculturales = Estudio.objects.filter(tipo="SC")

	cant_fisicos = estudios_fisicos.count()
	cant_biologicos = estudios_biologicos.count()
	cant_socioculturales = estudios_socioculturales.count()

	maximo = max([cant_fisicos, cant_biologicos, cant_socioculturales])
	lista = []
	for i in range(0, maximo):
		lista.append([])

	for i in range(0, maximo):
		if i < cant_fisicos:
			lista[i].append(estudios_fisicos[i])
		else:
			lista[i].append(None)
 
	for i in range(0, maximo):
		if i < cant_biologicos:
			lista[i].append(estudios_biologicos[i])
		else:   
			lista[i].append(None)

	print(lista)
	for i in range(0, maximo):
		if i < cant_socioculturales:
			lista[i].append(estudios_socioculturales[i])
		else:
			lista[i].append(None)

	return render(request, 'configuracion/index.html', {'lista':lista})

# Formulario para registrar un estudio/impacto
class EstudioCreate(CreateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'

	def get_success_url(self):
		if self.request.POST.get('editar'):
			return reverse('calcular_datos', args=(self.object.id,))

class EstudioUpdate(UpdateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'

	def get_success_url(self):
		if self.request.POST.get('editar'):
			return reverse('calcular_datos', args=(self.object.id,))
		elif self.request.POST.get('eliminar'):
			return reverse('eliminar_estudio', args=(self.object.id,))

def calcular_datos(request, pk):
	estudio = Estudio.objects.get(id=pk)
	via = estudio.intensidad*(estudio.pondIntensidad/100) + estudio.extension*(estudio.pondExtension/100) + estudio.duracion*(estudio.pondDuracion/100) + estudio.reversibilidad*(estudio.pondReversibilidad/100) + estudio.probabilidad*(estudio.pondProbabilidad/100)

	print(estudio.grado_perturbacion_intensidad)
	estudio.via = via
	estudio.save()

	return HttpResponseRedirect(reverse('index'))

def eliminar_estudio(request, pk):
	estudio = Estudio.objects.get(id=pk).delete()
	return HttpResponseRedirect(reverse('index'))



