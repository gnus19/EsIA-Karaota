from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from configuracion.forms import *
from configuracion.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

def modificar_tablas(request):

	return render(request, 'configuracion/modificar_tablas.html', {})

def tablas(request):
	intensidad_fuerte = Intensidad.objects.all().filter(grado_perturbacion='F')
	intensidad_medio = Intensidad.objects.all().filter(grado_perturbacion='M')
	intensidad_suave = Intensidad.objects.all().filter(grado_perturbacion='S')
	extension = Extension.objects.all().order_by('id')
	duracion = Duracion.objects.all().order_by('id')
	reversibilidad = Reversibilidad.objects.all().order_by('id')
	probabilidad = Probabilidad.objects.all().order_by('id')
	return render(request, 'configuracion/tablas.html', {'intensidad_fuerte':intensidad_fuerte, 'intensidad_medio':intensidad_medio, 'intensidad_suave':intensidad_suave, 'extension':extension, 'duracion':duracion, 'reversibilidad':reversibilidad, 'probabilidad':probabilidad})

# Index de los impactos y listado de los mismos
def index(request):
	#_insertar_datos()

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

	for i in range(0, maximo):
		if i < cant_socioculturales:
			lista[i].append(estudios_socioculturales[i])
		else:
			lista[i].append(None)

	return render(request, 'configuracion/index.html', {'lista':lista})

# Formulario para registrar un estudio/impacto
class EstudioCreate(CreateView, SuccessMessageMixin):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'
	success_url = reverse_lazy('index')

	# def form_valid(self, form):
	# 	self.object = form.save(commit=False)
	# 	print(self.request.nombre)
	# 	# val_intensidad = _calcular_intensidad(self.object)
	# 	# val_duracion = _calcular_duracion(self.object)
	# 	# val_reversibilidad = _calcular_reversibilidad(self.object)
	# 	# val_extension = _calcular_extension(s == elf.object)
	# 	# val_via = _calcular_via(self.object, val_intensidad, val_duracion, val_reversibilidad, val_extension)
	# 	# self.object.intensidad = val_intensidad
	# 	# self.object.duracion = val_duracion
	# 	# self.object.reversibilidad = val_reversibilidad
	# 	# self.object.extension = val_extension
	# 	# self.object.via = val_via
	# 	# self.object.importancia_estudio, self.object.valor_estudio = _calcular_importancia(val_via)
	# 	# self.object.save()
	# 	# messages.success(self.request, "Estudio agregado exitosamente", extra_tags='alert')
	# 	return super(ModelFormMixin, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)

		consulta_intensidad = Intensidad.objects.all()
		consulta_extension = Extension.objects.all()
		consulta_duracion = Duracion.objects.all()
		consulta_reversibilidad = Reversibilidad.objects.all()
		consulta_probabilidad = Probabilidad.objects.all()

		grado_perturbacion = request.POST.get('grado_perturbacion')
		valor_sa = request.POST.get('valor_sociocultural')
		ext_clasificacion =request.POST.get('clasificacion_extension')
		dur_criterios =request.POST.get('criterio_duracion')
		rev_clasificacion = request.POST.get('clasificacion_reversibilidad')
		probabilidad =request.POST.get('clasificacion_probabilidad')

		for i in consulta_intensidad:
			if i.valor_sociocultural == valor_sa and i.grado_perturbacion == grado_perturbacion:
				self.object.intensidad = i.id
				break

		for i in consulta_extension:
			if i.clasificacion == ext_clasificacion:
				self.object.extension = i.id
				break

		for i in consulta_duracion:
			if i.criterio == dur_criterios:
				self.object.duracion = i.id
				break

		for i in consulta_reversibilidad:
			if i.clasificacion == rev_clasificacion:
				self.object.reversibilidad = i.id
				break

		for i in consulta_probabilidad:
			if i.probabilidad == probabilidad:
				self.object.probabilidad = i.id
				break

		if form.is_valid():
			formulario = form.save(commit=False)
			formulario.save()
			return HttpResponseRedirect(self.get_success_url())

		else:
			return self.render_to_response(self.get_context_data(form=form))

	def grado_perturbacion(self):
		GRADO_PERTUBACION = ('Fuerte', 'Medio', 'Suave')
		return GRADO_PERTUBACION

	def valor_sa(self):
		VALOR_SA = ('Muy Alto', 'Alto', 'Medio', 'Bajo')
		return VALOR_SA

	def ext_clasificacion(self):
		EXT_CLASIFICACION = ('Generalizada (>75%)', 'Extensiva (35-74%)', 'Local (10-34%)', 'Puntual (<10%)')
		return EXT_CLASIFICACION

	def dur_criterios(self):
		DUR_CRITERIOS = ('Menos de 2 años', '2 a 5 años', '5 a 10 años', 'Mas de 10 años')
		return DUR_CRITERIOS

	def rev_clasificacion(self):
		REV_CLASIFICACION = ('Irreversible', 'Requiere Tratamiento', 'Medianamente Reversible', 'Reversible')
		return REV_CLASIFICACION

	def probabilidad(self):
		PROBABILIDAD = ('Alta', 'Media', 'Baja', 'Nula')
		return PROBABILIDAD

# # Actualizacion de los datos del formulario 
# class EstudioUpdate(UpdateView, SuccessMessageMixin):
# 	model = Estudio
# 	form_class = EstudioForm
# 	template_name = 'configuracion/agregar_estudio.html'
# 	success_message = "Datos del Estudio actualizados correctamente"

# 	def form_valid(self, form):
# 		if self.request.POST.get('editar'):
# 			self.object = form.save(commit=False)
# 			val_intensidad = _calcular_intensidad(self.object)
# 			val_duracion = _calcular_duracion(self.object)
# 			val_reversibilidad = _calcular_reversibilidad(self.object)
# 			val_extension = _calcular_extension(self.object)
# 			val_via = _calcular_via(self.object, val_intensidad, val_duracion, val_reversibilidad, val_extension)
# 			self.object.intensidad = val_intensidad
# 			self.object.duracion = val_duracion
# 			self.object.reversibilidad = val_reversibilidad
# 			self.object.extension = val_extension
# 			self.object.via = val_via
# 			self.object.importancia_estudio, self.object.valor_estudio = _calcular_importancia(val_via)
# 			self.object.save()
# 			messages.success(self.request, "Datos del estudio modificados exitosamente", extra_tags='alert')
# 		return super(ModelFormMixin, self).form_valid(form)

# 	# def get_context_data(self, **kwargs):
# 	# 	context = super(EstudioUpdate, self).get_context_data(**kwargs)
# 	# 	return context

# 	def get_success_url(self):
# 		if self.request.POST.get('editar'):
# 			return reverse('index')

# # # Calculo de la Valoracion de la Intensidad
# def _calcular_intensidad(estudio):
	
# 	if estudio.grado_perturbacion_intensidad == 'F':
# 		if estudio.valor_sociocultural_intensidad == 'MA':
# 			valor_intensidad = 10
# 		elif estudio.valor_sociocultural_intensidad == 'A':
# 			valor_intensidad = 7
# 		elif estudio.valor_sociocultural_intensidad == 'M':
# 			valor_intensidad = 5
# 		else:
# 			valor_intensidad = 5
# 	elif estudio.grado_perturbacion_intensidad == 'M':
# 		if estudio.valor_sociocultural_intensidad == 'MA' or estudio.valor_sociocultural_intensidad == 'A':
# 			valor_intensidad = 7
# 		elif estudio.valor_sociocultural_intensidad == 'M':
# 			valor_intensidad = 5
# 		else:
# 			valor_intensidad = 2
# 	else:
# 		if estudio.valor_sociocultural_intensidad == 'MA' or estudio.valor_sociocultural_intensidad == 'A':
# 			valor_intensidad = 5
# 		else:
# 			valor_intensidad = 5

# 	return valor_intensidad

# # Claculo de la Valoracion de la Extension
# def _calcular_extension(estudio):
	
# 	if estudio.clasificacion_extension == 'GE':
# 		valor_extension = 10
# 	elif estudio.clasificacion_extension == 'EX':
# 		valor_extension = 7
# 	elif estudio.clasificacion_extension == 'LO':
# 		valor_extension = 5
# 	else:
# 		valor_extension = 2

# 	return valor_extension

# # Calculo de la Valoracion de la Duracion
# def _calcular_duracion(estudio):
	
# 	if estudio.criterio_duracion == 'M2':
# 		valor_duracion = 2
# 	elif estudio.criterio_duracion == 'M2-5':
# 		valor_duracion = 5
# 	elif estudio.criterio_duracion == 'M5-10':
# 		valor_duracion = 7
# 	else:
# 		valor_duracion = 10

# 	return valor_duracion

# # Calculo de la Reversibilidad
# def _calcular_reversibilidad(estudio):
	
# 	if estudio.clasificacion_reversibilidad == 'IR':
# 		valor_reversibilidad = 10
# 	elif estudio.clasificacion_reversibilidad == 'TR':
# 		valor_reversibilidad = 7
# 	elif estudio.clasificacion_reversibilidad == 'MR':
# 		valor_reversibilidad = 5
# 	else:
# 		valor_reversibilidad = 2

# 	return valor_reversibilidad

# # Calculo del VIA
# def _calcular_via(estudio, valor_intensidad, valor_duracion, valor_reversibilidad, valor_extension):

# 	return valor_intensidad*(estudio.pondIntensidad/100) + valor_extension*(estudio.pondExtension/100) + valor_duracion*(estudio.pondDuracion/100) + valor_reversibilidad*(estudio.pondReversibilidad/100) + estudio.probabilidad*(estudio.pondProbabilidad/100)

# # Calculo de la importancia y valor de impacto del estudio
# def _calcular_importancia(via):

# 	if 0 <= via <= 2.9:
# 		importancia_estudio = 'Baja'
# 		valor_estudio = 2
# 	elif 3 <= via <= 5.9:
# 		importancia_estudio = 'Media'
# 		valor_estudio = 5
# 	elif 6 <= via <= 7.9:
# 		importancia_estudio = 'Alta'
# 		valor_estudio = 7
# 	elif 8 <= via:
# 		importancia_estudio = 'Muy Alta'
# 		valor_estudio = 10

# 	return importancia_estudio, valor_estudio

# # Funcion que elimina un estudio
# def eliminar_estudio(request, pk):
# 	estudio = Estudio.objects.get(id=pk).delete()
# 	messages.success(request, "Estudio eliminado exitosamente", extra_tags='alert')
# 	return HttpResponseRedirect(reverse('index'))

def _insertar_datos():
	if not Intensidad.objects.all():
		int_1 = Intensidad(valor_sociocultural='MA', grado_perturbacion='F', valor=10)
		int_2 = Intensidad(valor_sociocultural='MA', grado_perturbacion='M', valor=7)
		int_3 = Intensidad(valor_sociocultural='MA', grado_perturbacion='S', valor=5)
		int_4 = Intensidad(valor_sociocultural='A', grado_perturbacion='F', valor=7)
		int_5 = Intensidad(valor_sociocultural='A', grado_perturbacion='M', valor=7)
		int_6 = Intensidad(valor_sociocultural='A', grado_perturbacion='S', valor=5)
		int_7 = Intensidad(valor_sociocultural='M', grado_perturbacion='F', valor=5)
		int_8 = Intensidad(valor_sociocultural='M', grado_perturbacion='M', valor=5)
		int_9 = Intensidad(valor_sociocultural='M', grado_perturbacion='S', valor=2)
		int_10 = Intensidad(valor_sociocultural='B', grado_perturbacion='F', valor=2)
		int_11 = Intensidad(valor_sociocultural='B', grado_perturbacion='M', valor=2)
		int_12 = Intensidad(valor_sociocultural='B', grado_perturbacion='S', valor=2)

		int_1.save()
		int_2.save()
		int_3.save()
		int_4.save()
		int_5.save()
		int_6.save()
		int_7.save()
		int_8.save()
		int_9.save()
		int_10.save()
		int_11.save()
		int_12.save()