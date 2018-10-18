from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from configuracion.forms import *
from configuracion.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Index de los impactos y listado de los mismos
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
	success_url = reverse_lazy('index')
	success_messages = "Estudio creado exitosamente"

	def form_valid(self, form):
		self.object = form.save(commit=False)
		val_intensidad = _calcular_intensidad(self.object)
		val_duracion = _calcular_duracion(self.object)
		val_reversibilidad = _calcular_reversibilidad(self.object)
		val_extension = _calcular_extension(self.object)
		val_via = _calcular_via(self.object, val_intensidad, val_duracion, val_reversibilidad, val_extension)
		self.object.intensidad = val_intensidad
		self.object.duracion = val_duracion
		self.object.reversibilidad = val_reversibilidad
		self.object.extension = val_extension
		self.object.via = val_via
		self.object.importancia_estudio, self.object.valor_estudio = _calcular_importancia(val_via)
		self.object.save()
		return super(ModelFormMixin, self).form_valid(form)

	# def get_success_url(self):
	# 	if self.request.POST.get('editar'):
	# 		return reverse('calcular_datos', args=(self.object.id,))

# Actualizacion de los datos del formulario 
class EstudioUpdate(UpdateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		val_intensidad = _calcular_intensidad(self.object)
		val_duracion = _calcular_duracion(self.object)
		val_reversibilidad = _calcular_reversibilidad(self.object)
		val_extension = _calcular_extension(self.object)
		val_via = _calcular_via(self.object, val_intensidad, val_duracion, val_reversibilidad, val_extension)
		self.object.intensidad = val_intensidad
		self.object.duracion = val_duracion
		self.object.reversibilidad = val_reversibilidad
		self.object.extension = val_extension
		self.object.via = val_via
		self.object.importancia_estudio, self.object.valor_estudio = _calcular_importancia(val_via)
		self.object.save()
		return super(ModelFormMixin, self).form_valid(form)

	def get_success_url(self):
		if self.request.POST.get('editar'):
			return reverse('index')
		elif self.request.POST.get('eliminar'):
			return reverse('eliminar_estudio', args=(self.object.id,))

# # Calculo de la Valoracion de la Intensidad
def _calcular_intensidad(estudio):
	
	if estudio.grado_perturbacion_intensidad == 'F':
		if estudio.valor_sociocultural_intensidad == 'MA':
			valor_intensidad = 10
		elif estudio.valor_sociocultural_intensidad == 'A':
			valor_intensidad = 7
		elif estudio.valor_sociocultural_intensidad == 'M':
			valor_intensidad = 5
		else:
			valor_intensidad = 5
	elif estudio.grado_perturbacion_intensidad == 'M':
		if estudio.valor_sociocultural_intensidad == 'MA' or estudio.valor_sociocultural_intensidad == 'A':
			valor_intensidad = 7
		elif estudio.valor_sociocultural_intensidad == 'M':
			valor_intensidad = 5
		else:
			valor_intensidad = 2
	else:
		if estudio.valor_sociocultural_intensidad == 'MA' or estudio.valor_sociocultural_intensidad == 'A':
			valor_intensidad = 5
		else:
			valor_intensidad = 5

	return valor_intensidad

# Claculo de la Valoracion de la Extension
def _calcular_extension(estudio):
	
	if estudio.clasificacion_extension == 'GE':
		valor_extension = 10
	elif estudio.clasificacion_extension == 'EX':
		valor_extension = 7
	elif estudio.clasificacion_extension == 'LO':
		valor_extension = 5
	else:
		valor_extension = 2

	return valor_extension

# Calculo de la Valoracion de la Duracion
def _calcular_duracion(estudio):
	
	if estudio.criterio_duracion == 'M2':
		valor_duracion = 2
	elif estudio.criterio_duracion == 'M2-5':
		valor_duracion = 5
	elif estudio.criterio_duracion == 'M5-10':
		valor_duracion = 7
	else:
		valor_duracion = 10

	return valor_duracion

# Calculo de la Reversibilidad
def _calcular_reversibilidad(estudio):
	
	if estudio.clasificacion_reversibilidad == 'IR':
		valor_reversibilidad = 10
	elif estudio.clasificacion_reversibilidad == 'TR':
		valor_reversibilidad = 7
	elif estudio.clasificacion_reversibilidad == 'MR':
		valor_reversibilidad = 5
	else:
		valor_reversibilidad = 2

	return valor_reversibilidad

# Calculo del VIA
def _calcular_via(estudio, valor_intensidad, valor_duracion, valor_reversibilidad, valor_extension):

	return valor_intensidad*(estudio.pondIntensidad/100) + valor_extension*(estudio.pondExtension/100) + valor_duracion*(estudio.pondDuracion/100) + valor_reversibilidad*(estudio.pondReversibilidad/100) + estudio.probabilidad*(estudio.pondProbabilidad/100)

# Calculo de la importancia y valor de impacto del estudio
def _calcular_importancia(via):

	if 0 <= via <= 2.9:
		importancia_estudio = 'Baja'
		valor_estudio = 2
	elif 3 <= via <= 5.9:
		importancia_estudio = 'Media'
		valor_estudio = 5
	elif 6 <= via <= 7.9:
		importancia_estudio = 'Alta'
		valor_estudio = 7
	elif 8 <= via:
		importancia_estudio = 'Muy Alta'
		valor_estudio = 100

	return importancia_estudio, valor_estudio

# Funcion que elimina un estudio
def eliminar_estudio(request, pk):
	estudio = Estudio.objects.get(id=pk).delete()
	messages.success(request, "Estudio eliminado exitosamente")
	return HttpResponseRedirect(reverse('index'))