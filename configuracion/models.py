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

class Relevancia(models.Model):
	efecto = models.CharField(max_length=50)
	#valoracion = models.CharField(choices=NIVEL_RELEVANCIA)
	valoracion = models.CharField(max_length=6)
	tipo = models.CharField(choices=TIPO_RELEVANCIA, max_length=25)

class Intensidad(models.Model):
	gradoIntensidad = models.CharField(choices=GRADO_PERTUBACION, max_length=25)
	valoracionSA = models.CharField(choices=VALOR_SA, max_length=25)
	valor = models.IntegerField(blank=True)

class Extension(models.Model):
	clasificacion = models.CharField(choices=EXT_CLASIFICACION, max_length=25)
	valor = models.IntegerField(blank=True)

class Duracion(models.Model):
	criterio = models.CharField(choices=DUR_CRITERIOS, max_length=25)
	valor = models.IntegerField(blank=True)

class Reversibilidad(models.Model):
	clasificacion = models.CharField(choices=REV_CLASIFICACION, max_length=25)
	valor = models.IntegerField(blank=True)

class Estudio(models.Model):
	relevancia = models.ForeignKey(Relevancia, on_delete=models.PROTECT)
	intensidad = models.ForeignKey(Intensidad, on_delete=models.PROTECT)
	extension = models.ForeignKey(Extension, on_delete=models.PROTECT)
	duracion = models.ForeignKey(Duracion, on_delete=models.PROTECT)
	reversibilidad = models.ForeignKey(Reversibilidad, on_delete=models.PROTECT)
	probabilidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondIntensidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondExtension = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondDuracion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondReversibilidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondProbabilidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	via = models.FloatField(default=0, blank=True)

	