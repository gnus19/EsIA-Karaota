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
			'intensidad',
			'extension',
			'duracion',
			'reversibilidad',
			'probabilidad',
			'pondIntensidad',
			'pondExtension',
			'pondDuracion',
			'pondReversibilidad',
			'pondProbabilidad',
		]

		labels = {
			'nombre': 'Nombre',
			'tipo': 'Tipo de Estudio',
			'valoracion_relevancia' : 'Relevancia',
			'tipo_relevancia': 'Tipo de Relevancia',
			'intensidad': 'Intensidad',
			'extension': 'Extension',
			'duracion': 'Duracion',
			'reversibilidad': 'Reversibilidad',
			'probabilidad': 'Probabilidad',
			'pondIntensidad': 'Ponderacion de la Intensidad',
			'pondExtension': 'Ponderacion de la Extension',
			'pondDuracion': 'Ponderacion de la Duracion',
			'pondReversibilidad': 'Ponderacion de la Reversibilidad',
			'pondProbabilidad': 'Ponderacion de la Probabilidad',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'tipo': forms.Select(attrs={'class':'form-control', 'required':''}),
			'valoracion_relevancia':forms.Select(attrs={'class':'form-control', 'required':''}),
			'tipo_relevancia': forms.Select(attrs={'class':'form-control', 'required':''}),
			'intensidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'extension': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'duracion': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'reversibilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'probabilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondIntensidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondExtension': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondDuracion': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondReversibilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
			'pondProbabilidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
		}