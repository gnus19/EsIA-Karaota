from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from configuracion.forms import *
from configuracion.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

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

	def get_success_url(self):
		if self.request.POST.get('editar'):
			return reverse('calcular_datos', args=(self.object.id,))

# Actualizacion de los datos del formulario 
class EstudioUpdate(UpdateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'

	def get_success_url(self):
		if self.request.POST.get('editar'):
			return reverse('calcular_datos', args=(self.object.id,))
		elif self.request.POST.get('eliminar'):
			return reverse('eliminar_estudio', args=(self.object.id,))

# Funcion que calcula todos lo valores y VIA
def calcular_datos(request, pk):
	estudio = Estudio.objects.get(id=pk)

	# Calculo de la Valoracion de la Intensidad
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

	estudio.intensidad = valor_intensidad

	# Claculo de la Valoracion de la 
	if estudio.clasificacion_extension == 'GE':
		valor_extension = 10
	elif estudio.clasificacion_extension == 'EX':
		valor_extension = 7
	elif estudio.clasificacion_extension == 'LO':
		valor_extension = 5
	else:
		valor_extension = 2

	estudio.extension = valor_extension

	# Calculo de la Valoracion de la Duracion
	if estudio.criterio_duracion == 'M2':
		valor_duracion = 2
	elif estudio.criterio_duracion == 'M2-5':
		valor_duracion = 5
	elif estudio.criterio_duracion == 'M5-10':
		valor_duracion = 7
	else:
		valor_duracion = 10

	estudio.duracion = valor_duracion

	# Calculo de la Reversibilidad
	if estudio.clasificacion_reversibilidad == 'IR':
		valor_reversibilidad = 10
	elif estudio.clasificacion_reversibilidad == 'TR':
		valor_reversibilidad = 7
	elif estudio.clasificacion_reversibilidad == 'MR':
		valor_reversibilidad = 5
	else:
		valor_reversibilidad = 2

	estudio.reversibilidad = valor_reversibilidad

	# Calculo del VIA
	via = valor_intensidad*(estudio.pondIntensidad/100) + valor_extension*(estudio.pondExtension/100) + valor_duracion*(estudio.pondDuracion/100) + valor_reversibilidad*(estudio.pondReversibilidad/100) + estudio.probabilidad*(estudio.pondProbabilidad/100)

	estudio.via = via

	# Calculo de la importancia y valor de impacto del estudio
	if 0 <= via <= 2.9:
		estudio.importancia_estudio = 'Baja'
		estudio.valor_estudio = 2
	elif 3 <= via <= 5.9:
		estudio.importancia_estudio = 'Media'
		estudio.valor_estudio = 5
	elif 6 <= via <= 7.9:
		estudio.importancia_estudio = 'Alta'
		estudio.valor_estudio = 7
	elif 8 <= via:
		estudio.importancia_estudio = 'Muy Alta'
		estudio.valor_estudio = 10

	estudio.save()

	return HttpResponseRedirect(reverse('index'))

# Funcion que elimina un estudio
def eliminar_estudio(request, pk):
	estudio = Estudio.objects.get(id=pk).delete()
	return HttpResponseRedirect(reverse('index'))



