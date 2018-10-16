from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from configuracion.forms import *
from configuracion.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

#Create your views here.
def index(request):
	
	estudios_fisicos = Estudio.objects.get(tipo="FS")
	estudios_biologicos = Estudio.objects.get(tipo="BIO")
	estudios_socioculturales = Estudio.objects.get(tipo="SC")

	return render(request, 'configuracion/index.html', {'estudios_fisico':estudios_fisicos, 'estudios_biologicos':estudios_biologicos, 'estudios_socioculturales':estudios_socioculturales})

# Formulario para registrar un estudio/impacto
class EstudioCreate(CreateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'
	# success_url = reverse_lazy('index')

	def grado_pertubacion(self):
		return GRADO_PERTUBACION

	def valor_sa(self):
		return VALOR_SA

	def ext_clasificacion(self):
		return EXT_CLASIFICACION

	def dur_criterios(self):
		return DUR_CRITERIOS

	def rev_clasificacion(self):
		return REV_CLASIFICACION

	def get_success_url(self):
		return reverse('calcular_via', args=(self.object.id,))

class EstudioUpdate(UpdateView):
	model = Estudio
	form_class = EstudioForm
	template_name = 'configuracion/agregar_estudio.html'
	success_url = reverse_lazy('index')

	def get_success_url(self):
		if self.request.POST.get('editar'):
			return reverse('calcular_via', args=(self.object.id,))
		elif self.request.POST.get('eliminar'):
			return reverse('eliminar_estudio', args=(self.object.id,))

def calcular_via(request, pk):
	print("Este es el id creado"+str(pk))
	estudio = Estudio.objects.get(id=pk)
	via = estudio.intensidad*estudio.pondIntensidad + estudio.extension*estudio.pondExtension + estudio.duracion*estudio.pondDuracion + estudio.reversibilidad*estudio.pondReversibilidad + estudio.probabilidad*estudio.pondProbabilidad
	estudio.via = via
	estudio.save()

	return HttpResponseRedirect(reverse('index'))

def eliminar_estudio(request, pk):
	estudio = Estudio.objects.get(id=pk).delete()
	print("HO")
	return HttpResponseRedirect(reverse('index'))



