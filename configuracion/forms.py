from django import forms
from configuracion.models import *

class EstudioForm(forms.ModelForm):

	class Meta:
		model = Estudio
		fields = [
			'nombre',
			'tipo',
			'valoracion_relevancia',
			'tipo_relevancia',
			'probabilidad',
			'pondIntensidad',
			'pondExtension',
			'pondDuracion',
			'pondReversibilidad',
			'pondProbabilidad',
			'grado_perturbacion_intensidad',
			'valor_sociocultural_intensidad',
			'clasificacion_extension',
			'criterio_duracion',
			'clasificacion_reversibilidad',
		]

		labels = {
			'nombre': 'Nombre',
			'tipo': 'Tipo de Estudio',
			'valoracion_relevancia' : 'Relevancia',
			'tipo_relevancia': 'Tipo de Relevancia',
			'probabilidad': 'Probabilidad',
			'pondIntensidad': 'Ponderacion de la Intensidad',
			'pondExtension': 'Ponderacion de la Extension',
			'pondDuracion': 'Ponderacion de la Duracion',
			'pondReversibilidad': 'Ponderacion de la Reversibilidad',
			'pondProbabilidad': 'Ponderacion de la Probabilidad',
			'grado_perturbacion_intensidad': 'Grado de Perturbacion',
			'valor_sociocultural_intensidad': 'Valor Socio-Cultural',
			'clasificacion_extension': 'Tipo de Extension',
			'criterio_duracion': 'Criterio de la Duracion',
			'clasificacion_reversibilidad': 'Tipo de Reversibilidad',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'tipo': forms.Select(attrs={'class':'form-control', 'required':''}),
			'valoracion_relevancia':forms.Select(attrs={'class':'form-control', 'required':''}),
			'tipo_relevancia': forms.Select(attrs={'class':'form-control', 'required':''}),
			'probabilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondIntensidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondExtension': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondDuracion': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondReversibilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondProbabilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'grado_perturbacion_intensidad': forms.Select(attrs={'class':'form-control', 'required':''}),
			'valor_sociocultural_intensidad': forms.Select(attrs={'class':'form-control', 'required':''}),
			'clasificacion_extension': forms.Select(attrs={'class':'form-control', 'required':''}),
			'criterio_duracion': forms.Select(attrs={'class':'form-control', 'required':''}),
			'clasificacion_reversibilidad': forms.Select(attrs={'class':'form-control', 'required':''}),
			}

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa