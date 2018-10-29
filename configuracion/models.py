from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
NIVEL_RELEVANCIA = (
	('A', 'Alto'),
	('M', 'Medio'),
	('Bajo', 'Bajo'),
	)
TIPO_RELEVANCIA = (
	('DI', 'Directo'),
	('IN', 'Indirecto'),	
	)
GRADO_PERTUBACION = (
	('F' ,'Fuerte'),
	('M', 'Medio'),
	('S', 'Suave'),
	)
VALOR_SA = (
	('MA', 'Muy Alto'),
	('A', 'Alto'),
	('M', 'Medio'),
	('B', 'Bajo'),
	)
EXT_CLASIFICACION = (
	('GE', 'Generalizada (>75%)'),
	('EX', 'Extensiva (35-74%)'),
	('LO', 'Local (10-34%)'),
	('PU', 'Puntual (<10%)'),
	)
DUR_CRITERIOS = (
	('M2', 'Menos de 2 años'),
	('M2-5', '2 a 5 años'),
	('M5-10', '5 a 10 años'),
	('M10', 'mas de 10 años'),
	)
REV_CLASIFICACION = (
	('IR', 'Irreversible'),
	('TR', 'Requiere Tratamiento'),
	('MR', 'Medianamente Reversible'),
	('RE', 'Reversible'),
	)
MEDIOS = (
	('FS','Fisico'),
	('BIO','Biologico'), 
	('SC','Socio-Cultural')
	)

class Estudio(models.Model):
	nombre = models.CharField(max_length=40, default="", unique=True, error_messages={'unique':'Ya existe un Estudio con el nombre colocado', 'max_length':'El nombre no puede pasar de mas de 40 caracteres'})
	tipo = models.CharField(choices=MEDIOS, max_length=50, default="")
	valoracion_relevancia = models.CharField(choices=NIVEL_RELEVANCIA, max_length=6, default="")
	tipo_relevancia = models.CharField(choices=TIPO_RELEVANCIA, max_length=50, default="")
	grado_perturbacion_intensidad = models.CharField(choices=GRADO_PERTUBACION, max_length=50, default="")
	valor_sociocultural_intensidad = models.CharField(choices=VALOR_SA, max_length=50, default="")
	intensidad = models.IntegerField(default=0)
	clasificacion_extension = models.CharField(choices=EXT_CLASIFICACION, max_length=50, default="")
	extension =  models.IntegerField(default=0)
	criterio_duracion = models.CharField(choices=DUR_CRITERIOS, max_length=50, default="")
	duracion = models.IntegerField(default=0)
	clasificacion_reversibilidad = models.CharField(choices=REV_CLASIFICACION, max_length=50, default="") 
	reversibilidad = models.IntegerField(default=0)
	probabilidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
	pondIntensidad = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondExtension = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondDuracion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondReversibilidad = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondProbabilidad = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	via = models.FloatField(default=0.0)
	importancia_estudio =  models.CharField(max_length=50, default="")
	valor_estudio = models.IntegerField(default=0)

class Intensidad(models.Model):
	tipo = models.CharField(max_length=40, default="", error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',})
	grado_perturbacion = models.CharField(max_length=40, default="", error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',})
	valor = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
	
class Extension(models.Model):
	tipo = models.CharField(max_length=40, default="", error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',})
	clasificacion = models.CharField(max_length=40, default="", error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',})
	valor = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
	
class Clasificacion(models.Model):
	tipo = models.CharField(max_length=40, default="", error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',})
	valor = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])	
	
class Reversibilidad(models.Model):
	tipo = models.CharField(max_length=40, default="", error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',})
	valor = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])	
		
class Ponderacion(models.Model):
	tipo = models.CharField(max_length=40, default="", error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',})
	valor = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])		
	
	
	