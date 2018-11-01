""" Models de Configuracion
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
NIVEL_RELEVANCIA = (
    ('A', 'Alto'),
    ('M', 'Medio'),
    ('B', 'Bajo'),
    )
TIPO_RELEVANCIA = (
    ('DI', 'Directo'),
    ('IN', 'Indirecto'),
    )
GRADO_PERTUBACION = (
    ('F', 'Fuerte'),
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
    ('M10', 'Mas de 10 años'),
    )
REV_CLASIFICACION = (
    ('IR', 'Irreversible'),
    ('TR', 'Requiere Tratamiento'),
    ('MR', 'Medianamente Reversible'),
    ('RE', 'Reversible'),
    )
PROBABILIDAD = (
    ('A', 'Alta'),
    ('M', 'Media'),
    ('B', 'Baja'),
    ('N', 'Nula'),
    )
NIVEL_IMPORTANCIA = (
    ('MA', 'Muy Alta'),
    ('A', 'Alta'),
    ('M', 'Media'),
    ('B', 'Baja'),
    )
MEDIOS = (
    ('FS', 'Fisico'),
    ('BIO', 'Biologico'),
    ('SC', 'Socio-Cultural'),
    )

class Intensidad(models.Model):
    """Tabla Intensidad
    """
    valor_sociocultural = models.CharField(
        choices=VALOR_SA,
        max_length=40,
        default="",
        error_messages={'max_length' : 'El nombre no puede pasar de mas de 40 caracteres',}
        )
    grado_perturbacion = models.CharField(
        choices=GRADO_PERTUBACION,
        max_length=40,
        default="",
        error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',}
        )
    valor = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )

    class Meta:
        """Meta de Intensidad
        """

        unique_together = (
            ('valor_sociocultural',
             'grado_perturbacion'),
            )

class Extension(models.Model):
    """Tabla Estudio
    """
    clasificacion = models.CharField(
        choices=EXT_CLASIFICACION,
        max_length=40,
        unique=True,
        default="",
        error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',}
        )
    valor = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )

class Duracion(models.Model):
    """Tabla Duracion
    """
    criterio = models.CharField(
        choices=DUR_CRITERIOS,
        unique=True,
        max_length=40,
        default="",
        error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',}
        )
    valor = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )

class Reversibilidad(models.Model):
    """Tabla Reversibilidad
    """
    clasificacion = models.CharField(
        choices=REV_CLASIFICACION,
        unique=True,
        max_length=40,
        default="",
        error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',}
        )
    valor = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )

class Probabilidad(models.Model):
    """Tabla Probabilidad
    """
    probabilidad = models.CharField(
        choices=PROBABILIDAD,
        unique=True,
        max_length=40,
        default="",
        error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',}
        )
    valor = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )

class Importancia(models.Model):
    """Tabla Importancia
    """
    importancia = models.CharField(
        choices=NIVEL_IMPORTANCIA,
        unique=True,
        max_length=40,
        default="",
        error_messages={'max_length':'El nombre no puede pasar de mas de 40 caracteres',}
        )
    minimo = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )
    maximo = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )
    valor = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )

class Estudio(models.Model):
    """Tabla Estudio
    """
    nombre = models.CharField(
        max_length=40,
        default="",
        unique=True,
        error_messages={'unique':'Ya existe un Estudio con el nombre colocado'}
        )
    tipo = models.CharField(
        choices=MEDIOS,
        max_length=50,
        default=""
        )
    valoracion_relevancia = models.CharField(
        choices=NIVEL_RELEVANCIA,
        max_length=6,
        default=""
        )
    tipo_relevancia = models.CharField(
        choices=TIPO_RELEVANCIA,
        max_length=50,
        default=""
        )
    intensidad = models.ForeignKey(
        Intensidad,
        default='',
        on_delete=models.PROTECT
        )
    extension = models.ForeignKey(
        Extension,
        default='',
        on_delete=models.PROTECT
        )
    duracion = models.ForeignKey(
        Duracion,
        default='',
        on_delete=models.PROTECT
        )
    reversibilidad = models.ForeignKey(
        Reversibilidad,
        default='',
        on_delete=models.PROTECT
        )
    probabilidad = models.ForeignKey(
        Probabilidad,
        default='',
        on_delete=models.PROTECT
        )
    pondIntensidad = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
        )
    pondExtension = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
        )
    pondDuracion = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
        )
    pondReversibilidad = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
        )
    pondProbabilidad = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
        )
    via = models.FloatField(
        default=0.0
        )
    importancia_estudio = models.ForeignKey(
        Importancia,
        default='',
        on_delete=models.PROTECT
        )
