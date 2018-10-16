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
	nombre = models.CharField(max_length=100, default="")
	tipo = models.CharField(choices=MEDIOS, max_length=25, default="")
	valoracion_relevancia = models.CharField(choices=NIVEL_RELEVANCIA, max_length=6, default="")
	tipo_relevancia = models.CharField(choices=TIPO_RELEVANCIA, max_length=25, default="")
	intensidad = models.IntegerField()
	extension =  models.IntegerField()
	duracion = models.IntegerField()
	duracion = models.IntegerField()
	reversibilidad = models.IntegerField()
	probabilidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondIntensidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondExtension = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondDuracion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondReversibilidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	pondProbabilidad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	via = models.FloatField(default=0.0)

	