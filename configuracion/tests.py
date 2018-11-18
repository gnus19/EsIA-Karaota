"""
Pruebas Unitarias
"""
import time
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from selenium.webdriver.support.ui import Select
from configuracion.models import NIVEL_RELEVANCIA, TIPO_RELEVANCIA, GRADO_PERTUBACION,VALOR_SA,EXT_CLASIFICACION,DUR_CRITERIOS,REV_CLASIFICACION,NIVEL_IMPORTANCIA,PROBABILIDAD,MEDIOS
from configuracion.views import _calcular_via
from configuracion.forms import EstudioForm
from configuracion.models import Intensidad,Probabilidad,Extension,Duracion,Reversibilidad,Importancia,Estudio
from utils.testutils import SeleniumTestCase

class KaraotaTests(TestCase):
    """
    Django Test
    """

    def setUp(self):
        """
        SetUp
        """
        self.client = Client() #Pruebas con testing tools de django

    def tearDown(self):
        """
        teardown
        """
        self.client = None
    def test_database_estudio(self):
        MyObject = type('MyObject', (object,), {})
        v_test = MyObject()
        v_test.pondIntensidad = 0
        v_test.pondExtension = 0
        v_test.pondDuracion = 0
        v_test.pondReversibilidad = 0
        v_test.pondProbabilidad = 0
     

    def test_ponderaciones_iguala101(self):
        """
        test_ponderacionesigual101
        """
        valores = {
            'nombre': 'Nombre 1',
            'tipo': 'FS',
            'valoracion_relevancia': 'MA',
            'tipo_relevancia': 'DI',
            # 'intensidad': intensidad,
            # 'extension': extension,
            # 'duracion': duracion,
            # 'reversibilidad': reversibilidad,
            # 'probabilidad': probabilidad,
            'pondIntensidad': 21,
            'pondExtension': 20,
            'pondDuracion': 20,
            'pondReversibilidad': 20,
            'pondProbabilidad': 20,
            # 'via': 5.0,
            # 'importancia_estudio': importancia

        }
        form = EstudioForm(data=valores)

        self.assertFalse(form.is_valid())

    def test_via_cota_inferior(self):
        """
        VIA inferior bien calculado
        """

        MyObject = type('MyObject', (object,), {})
        v_test = MyObject()
        v_test.pondIntensidad = 0
        v_test.pondExtension = 0
        v_test.pondDuracion = 0
        v_test.pondReversibilidad = 0
        v_test.pondProbabilidad = 0

        via = _calcular_via(v_test, 0, 0, 0, 0, 0)

        self.assertEqual(via, 0.0)

    def test_via_cota_superior(self):
        """
        VIA superior bien calculado
        """

        MyObject = type('MyObject', (object,), {})
        v_test = MyObject()
        v_test.pondIntensidad = 10
        v_test.pondExtension = 10
        v_test.pondDuracion = 10
        v_test.pondReversibilidad = 10
        v_test.pondProbabilidad = 10

        via = _calcular_via(v_test, 10, 10, 10, 10, 10)

        self.assertEqual(via, 5.0)

    def test_no_cambiaron_nivel_relevancia(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """

        nivel_relevancia_2 = (
            ('A', 'Alto'),
            ('M', 'Medio'),
            ('B', 'Bajo'),
            )

        self.assertEqual(NIVEL_RELEVANCIA[0][0], nivel_relevancia_2[0][0])
        self.assertEqual(NIVEL_RELEVANCIA[1][0], nivel_relevancia_2[1][0])
        self.assertEqual(NIVEL_RELEVANCIA[2][0], nivel_relevancia_2[2][0])

        self.assertEqual(NIVEL_RELEVANCIA[0][1], nivel_relevancia_2[0][1])
        self.assertEqual(NIVEL_RELEVANCIA[1][1], nivel_relevancia_2[1][1])
        self.assertEqual(NIVEL_RELEVANCIA[2][1], nivel_relevancia_2[2][1])

    def test_no_cambiaron_tipo_relevancia(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """
        tipo_relevancia_2 = (
            ('DI', 'Directo'),
            ('IN', 'Indirecto'),
        )
        self.assertEqual(TIPO_RELEVANCIA[0][0], tipo_relevancia_2[0][0])
        self.assertEqual(TIPO_RELEVANCIA[1][0], tipo_relevancia_2[1][0])

        self.assertEqual(TIPO_RELEVANCIA[0][1], tipo_relevancia_2[0][1])
        self.assertEqual(TIPO_RELEVANCIA[1][1], tipo_relevancia_2[1][1])

    def test_no_cambiaron_grado_perturbacion(self):
        """
            se verifica que nadie cambio el nivel de relevancia
        """
        grado_pertubacion_2 = (
            ('F', 'Fuerte'),
            ('M', 'Medio'),
            ('S', 'Suave'),
        )
        self.assertEqual(GRADO_PERTUBACION[0][0], grado_pertubacion_2[0][0])
        self.assertEqual(GRADO_PERTUBACION[1][0], grado_pertubacion_2[1][0])
        self.assertEqual(GRADO_PERTUBACION[2][0], grado_pertubacion_2[2][0])

        self.assertEqual(GRADO_PERTUBACION[0][1], grado_pertubacion_2[0][1])
        self.assertEqual(GRADO_PERTUBACION[1][1], grado_pertubacion_2[1][1])
        self.assertEqual(GRADO_PERTUBACION[2][1], grado_pertubacion_2[2][1])
		
    def test_no_cambiaron_valor_sa(self):
        """
            se verifica que nadie cambio los valores_sa
        """
        valor_sa_2 = (
            ('MA', 'Muy Alto'),
            ('A', 'Alto'),
            ('M', 'Medio'),
            ('B', 'Bajo'),
        )
        self.assertEqual(VALOR_SA[0][0], valor_sa_2[0][0])
        self.assertEqual(VALOR_SA[1][0], valor_sa_2[1][0])
        self.assertEqual(VALOR_SA[2][0], valor_sa_2[2][0])
        self.assertEqual(VALOR_SA[3][0], valor_sa_2[3][0])
		
        self.assertEqual(VALOR_SA[0][1], valor_sa_2[0][1])
        self.assertEqual(VALOR_SA[1][1], valor_sa_2[1][1])
        self.assertEqual(VALOR_SA[2][1], valor_sa_2[2][1])
        self.assertEqual(VALOR_SA[3][1], valor_sa_2[3][1])
		
    def test_no_cambiaron_ext_clasificacion(self):
        """
            se verifica que nadie cambio ext_clasificacion
        """
        ext = (
            ('GE', 'Generalizada (>75%)'),
            ('EX', 'Extensiva (35-74%)'),
            ('LO', 'Local (10-34%)'),
            ('PU', 'Puntual (<10%)'),
            )
        self.assertEqual(EXT_CLASIFICACION[0][0], ext[0][0])
        self.assertEqual(EXT_CLASIFICACION[1][0], ext[1][0])
        self.assertEqual(EXT_CLASIFICACION[2][0], ext[2][0])
        self.assertEqual(EXT_CLASIFICACION[3][0], ext[3][0])
		
        self.assertEqual(EXT_CLASIFICACION[0][1], ext[0][1])
        self.assertEqual(EXT_CLASIFICACION[1][1], ext[1][1])
        self.assertEqual(EXT_CLASIFICACION[2][1], ext[2][1])
        self.assertEqual(EXT_CLASIFICACION[3][1], ext[3][1])
		
    def test_no_cambiaron_dur_criterios(self):
        """
            se verifica que nadie cambio dur_clasifiacion
        """
        dur = (
            ('M2', 'Menos de 2 años'),
            ('M2-5', '2 a 5 años'),
            ('M5-10', '5 a 10 años'),
            ('M10', 'Mas de 10 años'),
            )
        self.assertEqual(DUR_CRITERIOS[0][0], dur[0][0])
        self.assertEqual(DUR_CRITERIOS[1][0], dur[1][0])
        self.assertEqual(DUR_CRITERIOS[2][0], dur[2][0])
        self.assertEqual(DUR_CRITERIOS[3][0], dur[3][0])

        self.assertEqual(DUR_CRITERIOS[0][1], dur[0][1])
        self.assertEqual(DUR_CRITERIOS[1][1], dur[1][1])
        self.assertEqual(DUR_CRITERIOS[2][1], dur[2][1])
        self.assertEqual(DUR_CRITERIOS[3][1], dur[3][1])	

    def test_no_cambiaron_rev_clasificacion(self):
        """
            se verifica que nadie cambio rev_clasificacion
        """
        rev = (
            ('IR', 'Irreversible'),
            ('TR', 'Requiere Tratamiento'),
            ('MR', 'Medianamente Reversible'),
            ('RE', 'Reversible'),
            )
        self.assertEqual(REV_CLASIFICACION[0][0], rev[0][0])
        self.assertEqual(REV_CLASIFICACION[1][0], rev[1][0])
        self.assertEqual(REV_CLASIFICACION[2][0], rev[2][0])
        self.assertEqual(REV_CLASIFICACION[3][0], rev[3][0])
		
        self.assertEqual(REV_CLASIFICACION[0][1], rev[0][1])
        self.assertEqual(REV_CLASIFICACION[1][1], rev[1][1])
        self.assertEqual(REV_CLASIFICACION[2][1], rev[2][1])				
        self.assertEqual(REV_CLASIFICACION[3][1], rev[3][1])
		
    def test_no_cambiaron_probabilidad(self):
        """
            se verifica que nadie cambio rev_clasificacion
        """
        pro = (
            ('A', 'Alta'),
            ('M', 'Media'),
            ('B', 'Baja'),
            ('N', 'Nula'),
            )
        self.assertEqual(PROBABILIDAD[0][0], pro[0][0])
        self.assertEqual(PROBABILIDAD[1][0], pro[1][0])
        self.assertEqual(PROBABILIDAD[2][0], pro[2][0])
        self.assertEqual(PROBABILIDAD[3][0], pro[3][0])
		
        self.assertEqual(PROBABILIDAD[0][1], pro[0][1])
        self.assertEqual(PROBABILIDAD[1][1], pro[1][1])
        self.assertEqual(PROBABILIDAD[2][1], pro[2][1])				
        self.assertEqual(PROBABILIDAD[3][1], pro[3][1])								
		
    def test_no_cambiaron_nivel_importancia(self):
        """
            se verifica que nadie cambio rev_clasificacion
        """
        niv = (
            ('MA', 'Muy Alta'),
            ('A', 'Alta'),
            ('M', 'Media'),
            ('B', 'Baja'),
            )
        self.assertEqual(NIVEL_IMPORTANCIA[0][0], niv[0][0])
        self.assertEqual(NIVEL_IMPORTANCIA[1][0], niv[1][0])
        self.assertEqual(NIVEL_IMPORTANCIA[2][0], niv[2][0])
        self.assertEqual(NIVEL_IMPORTANCIA[3][0], niv[3][0])
		
        self.assertEqual(NIVEL_IMPORTANCIA[0][1], niv[0][1])
        self.assertEqual(NIVEL_IMPORTANCIA[1][1], niv[1][1])
        self.assertEqual(NIVEL_IMPORTANCIA[2][1], niv[2][1])				
        self.assertEqual(NIVEL_IMPORTANCIA[3][1], niv[3][1])	
		
    def test_no_cambiaron_medios(self):
        """
            se verifica que nadie cambio rev_clasificacion
        """
        med = (
            ('FS', 'Fisico'),
            ('BIO', 'Biologico'),
            ('SC', 'Socio-Cultural'),
            )		
        self.assertEqual(MEDIOS[0][0], med[0][0])
        self.assertEqual(MEDIOS[1][0], med[1][0])
        self.assertEqual(MEDIOS[2][0], med[2][0])

        self.assertEqual(MEDIOS[0][1], med[0][1])
        self.assertEqual(MEDIOS[1][1], med[1][1])
        self.assertEqual(MEDIOS[2][1], med[2][1])				
			
    def test_http_reponse_ok_tabla(self):
        """
        Estatus Ok HTTP de la pagina de la tabla
        """
        response = self.client.get('/configuracion/index/')
        self.assertEqual(response.status_code, 200)

    def test_templates_correctos_tabla(self):
        """
            Carga exitosa de los Templates
        """
        response = self.client.get('/configuracion/index/')
        self.assertTemplateUsed(response, 'configuracion/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_formulario(self):
        """
        Estatu Ok HTTP del formulario
        """
        response = self.client.get('/configuracion/agregar_estudio/')
        self.assertEqual(response.status_code, 200)

    def test_templates_correctos_formulario(self):
        """
        Carga exitosa de los Templates
        """
        response = self.client.get('/configuracion/agregar_estudio/')
        self.assertTemplateUsed(response, 'configuracion/agregar_estudio.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_tablas(self):
        """
        Estatu Ok HTTP del formulario
        """
        response = self.client.get('/configuracion/tablas/')
        self.assertEqual(response.status_code, 200)

    def test_templates_correctos_tablas(self):
        """
        Carga exitosa de los Templates
        """
        response = self.client.get('/configuracion/tablas/')
        self.assertTemplateUsed(response, 'configuracion/tablas.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_http_reponse_ok_modificar_tablas(self):
        """
        Estatu Ok HTTP del formulario
        """
        response = self.client.get('/configuracion/tablas/')
        self.assertEqual(response.status_code, 200)

    def test_templates_correctos_modificar_tablas(self):
        """
            Carga exitosa de los Templates
        """
        response = self.client.get('/configuracion/modificar_tablas/')
        self.assertTemplateUsed(response, 'configuracion/modificar_tablas.html')
        self.assertTemplateUsed(response, 'base.html')

class TestsIntegridadDatosTablasEstudio(TestCase):
    def setUp(self):
        '''Se crean instancias para las pruebas'''
		
		#Intensidad
        self.intensidad = [[None,None,None],[None,None,None],[None,None,None],[None,None,None]]
        self.intensidad[0][0]=Intensidad.objects.filter(valor_sociocultural="MA",grado_perturbacion="F").first()
        self.intensidad[0][1]=Intensidad.objects.filter(valor_sociocultural="MA",grado_perturbacion="M").first()  
        self.intensidad[0][2]=Intensidad.objects.filter(valor_sociocultural="MA",grado_perturbacion="S").first()  
		
        self.intensidad[1][0]=Intensidad.objects.filter(valor_sociocultural="A",grado_perturbacion="F").first()  
        self.intensidad[1][1]=Intensidad.objects.filter(valor_sociocultural="A",grado_perturbacion="M").first()  
        self.intensidad[1][2]=Intensidad.objects.filter(valor_sociocultural="A",grado_perturbacion="S").first()  

        self.intensidad[2][0]=Intensidad.objects.filter(valor_sociocultural="M",grado_perturbacion="F").first()  
        self.intensidad[2][1]=Intensidad.objects.filter(valor_sociocultural="M",grado_perturbacion="M").first()  
        self.intensidad[2][2]=Intensidad.objects.filter(valor_sociocultural="M",grado_perturbacion="S").first()  
		
        self.intensidad[3][0]=Intensidad.objects.filter(valor_sociocultural="B",grado_perturbacion="F").first()  
        self.intensidad[3][1]=Intensidad.objects.filter(valor_sociocultural="B",grado_perturbacion="M").first()  
        self.intensidad[3][2]=Intensidad.objects.filter(valor_sociocultural="B",grado_perturbacion="S").first()  	

        #Extension
        self.extension = [None,None,None,None]
        self.extension[0] = Extension.objects.filter(clasificacion="GE").first()
        self.extension[1] = Extension.objects.filter(clasificacion="EX").first()
        self.extension[2] = Extension.objects.filter(clasificacion="LO").first()
        self.extension[3] = Extension.objects.filter(clasificacion="PU").first()


        #Duracion
        self.duracion = [None,None,None,None]

        self.duracion[0] = Duracion.objects.filter(criterio="M10").first()
        self.duracion[1] = Duracion.objects.filter(criterio="M5-10").first()
        self.duracion[2] = Duracion.objects.filter(criterio="M2-5").first()
        self.duracion[3] = Duracion.objects.filter(criterio="M2").first()
		
        #Reversibilidad
        self.reversibilidad = [None,None,None,None]
        self.reversibilidad[0] = Reversibilidad.objects.filter(clasificacion="IR").first()
        self.reversibilidad[1] = Reversibilidad.objects.filter(clasificacion="TR").first()
        self.reversibilidad[2] = Reversibilidad.objects.filter(clasificacion="MR").first()
        self.reversibilidad[3] = Reversibilidad.objects.filter(clasificacion="RE").first()

        #Importancia
        self.importancia = [None,None,None,None]
        self.importancia[0] = Importancia.objects.filter(importancia="MA").first()
        self.importancia[1] = Importancia.objects.filter(importancia="A").first()
        self.importancia[2] = Importancia.objects.filter(importancia="M").first()
        self.importancia[3] = Importancia.objects.filter(importancia="B").first()
		
		#Probabilidad

        self.probabilidad = [None,None,None,None]
        self.probabilidad[0] = Probabilidad.objects.filter(probabilidad="A").first()
        self.probabilidad[1] = Probabilidad.objects.filter(probabilidad="M").first()
        self.probabilidad[2] = Probabilidad.objects.filter(probabilidad="B").first()
        self.probabilidad[3] = Probabilidad.objects.filter(probabilidad="N").first()

    def test_intensidad_transitividad_MA(self):
        self.assertTrue(self.intensidad[0][0].valor>= self.intensidad[0][1].valor and self.intensidad[0][1].valor >= self.intensidad[0][2].valor )	

    def test_intensidad_limites_MA(self):

        self.assertTrue(self.intensidad[1][0].valor>= 0 and self.intensidad[1][2].valor<=10)		
		
    def test_intensidad_transitividad_A(self):
        self.assertTrue(self.intensidad[1][0].valor>= self.intensidad[1][1].valor and self.intensidad[1][1].valor >= self.intensidad[1][2].valor )	

    def test_intensidad_limites_A(self):

        self.assertTrue(self.intensidad[1][0].valor>= 0 and self.intensidad[1][2].valor<=10)	
		
    def test_intensidad_transitividad_M(self):
        self.assertTrue(self.intensidad[2][0].valor>= self.intensidad[2][1].valor and self.intensidad[2][1].valor >= self.intensidad[2][2].valor )	

    def test_intensidad_limites_M(self):

        self.assertTrue(self.intensidad[2][0].valor>= 0 and self.intensidad[2][2].valor<=10)			
		
    def test_intensidad_transitividad_B(self):
        self.assertTrue(self.intensidad[3][0].valor>= self.intensidad[3][1].valor and self.intensidad[3][1].valor >= self.intensidad[3][2].valor )	

    def test_intensidad_limites_B(self):

        self.assertTrue(self.intensidad[3][0].valor>= 0 and self.intensidad[3][2].valor<=10)
		
    def test_extension_transitividad(self):

        self.assertTrue(self.extension[0].valor>= self.extension[1].valor and self.extension[1].valor >= self.extension[2].valor and self.extension[2].valor>= self.extension[3].valor)	
		
    def test_extension_limites(self):

        self.assertTrue(self.extension[0].valor>= 0 and self.extension[3].valor<=10)					

    def test_duracion_transitividad(self):

        self.assertTrue(self.duracion[0].valor>= self.duracion[1].valor and self.duracion[1].valor >= self.duracion[2].valor and self.duracion[2].valor>= self.duracion[3].valor)	
		
    def test_duracion_limites(self):

        self.assertTrue(self.duracion[0].valor>= 0 and self.duracion[3].valor<=10)					
		
    def test_reversibilidad_transitividad(self):

        self.assertTrue(self.reversibilidad[0].valor>= self.reversibilidad[1].valor and self.reversibilidad[1].valor >= self.reversibilidad[2].valor and self.reversibilidad[2].valor>= self.reversibilidad[3].valor)	
		
    def test_reversibilidad_limites(self):

        self.assertTrue(self.reversibilidad[0].valor>= 0 and self.reversibilidad[3].valor<=10)					
		
    def test_importancia_transitividad(self):

        self.assertTrue(self.importancia[0].valor>= self.importancia[1].valor and self.importancia[1].valor >= self.importancia[2].valor and self.importancia[2].valor>= self.importancia[3].valor)	
		
    def test_importancia_limites(self):

        self.assertTrue(self.importancia[0].valor>= 0 and self.importancia[3].valor<=10)					
						
    def test_probabilidad_transitividad(self):

        self.assertTrue(self.probabilidad[0].valor>= self.probabilidad[1].valor and self.probabilidad[1].valor >= self.probabilidad[2].valor and self.probabilidad[2].valor>= self.probabilidad[3].valor)	
		
    def test_probabilidad_limites(self):

        self.assertTrue(self.probabilidad[0].valor>= 0 and self.probabilidad[3].valor<=100)			
		
		
class TestsEstudio(TestCase):	
			
    def test_insertar_estudio(self):
        intensidad2 = Intensidad.objects.filter(valor_sociocultural="MA",grado_perturbacion="F").first()
        extension2=Extension.objects.filter(clasificacion="GE").first()
        duracion2=Duracion.objects.filter(criterio="M10").first()
        reversibilidad2=Reversibilidad.objects.filter(clasificacion="IR").first()
        importancia2=Importancia.objects.filter(importancia="MA").first()
        probabilidad2=Probabilidad.objects.filter(probabilidad="A").first()		
		
        est = Estudio.objects.create(
            nombre="test_estudio",
			tipo="FS",
			valoracion_relevancia="MA",
			tipo_relevancia="DI",
			intensidad=intensidad2,
			extension = extension2,
			duracion = duracion2,
			reversibilidad = reversibilidad2,
			probabilidad = probabilidad2,
			pondIntensidad="20",
			pondExtension="20",
			pondDuracion="20",
			pondReversibilidad="20",
			pondProbabilidad="20",
			via="5",
			importancia_estudio = importancia2
		)
		

        est2 = Estudio.objects.filter(nombre="test_estudio").first()      		
		
        self.assertEqual(est.id,est2.id)			
		
 


class PruebaFormularioEstudio(SeleniumTestCase):
    """
    Prueba Formulario Estudio
    """
    fixtures = ['users-and-groups.json']


    def test_navegador(self): #pylint: disable=too-many-statements
        """
        test del navegador
        """
        self.selenium.get('{}{}'.format(self.live_server_url, reverse('dashboard:index')))
        self.selenium.find_element_by_id('id_username').send_keys('admin')
        self.selenium.find_element_by_id('id_password').send_keys('jaja1234')
        self.selenium.find_element_by_id('id_submit').click()

        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        # Volvemos a agregar otro elemento pero ahora de tipo Biologico
        self.selenium.find_element_by_css_selector('#agregar-estudio').click()
        nombre = "Impacto F"
        self.selenium.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        select_tipo = Select(self.selenium.find_element_by_name('tipo'))
        select_tipo.select_by_visible_text('Fisico')
        self.selenium.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        #agregamos la ponderacion de la intensidad
        self.selenium.find_element_by_name('pondIntensidad').send_keys(20)
        #agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(20)
        #agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(30)
        #agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(10)
        #agregamos la ponderacion de la probabilidad
        self.selenium.find_element_by_name('pondProbabilidad').send_keys(20)
        # Hacemos click en agregar
        self.selenium.find_element_by_name('editar').click()
        #para las alertas del navegador
        confirmacion = self.selenium.switch_to.alert
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        # Volvemos a agregar otro elemento pero ahora de tipo Biologico
        # Hacemos click en agregar
        self.selenium.find_element_by_css_selector('#agregar-estudio').click()
        nombre = "Impacto B"
        #agregamos el nombre
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        select_tipo = Select(self.selenium.find_element_by_name('tipo'))
        # select_tipo.select_by_visible_text('Biologico')
        #movemos el scroll un poco
        self.selenium.execute_script("window.scrollTo(0, 720)")
        #agregamos la ponderacion de la intensidad
        self.selenium.find_element_by_name('pondIntensidad').send_keys(20)
        #agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(20)
        #agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(30)
        #agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(10)

        # agregamos la ponderacion de la probabilidad
        self.selenium.find_element_by_name('pondProbabilidad').send_keys(20)
        self.selenium.find_element_by_name('editar').click() # Hacemos click en agregar
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        # Volvemos a agregar otro elemento pero ahora de tipo Socio-Cultural
        self.selenium.find_element_by_css_selector('#agregar-estudio').click()
        nombre = "Impacto SC"
        self.selenium.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        select_tipo = Select(self.selenium.find_element_by_name('tipo'))
        # select_tipo.select_by_visible_text('Socio-Cultural')
        #movemos el scroll un poco
        self.selenium.execute_script("window.scrollTo(0, 720)")
        #agregamos la ponderacion de la intensidad
        self.selenium.find_element_by_name('pondIntensidad').send_keys(20)
        #agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(20)
        #agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(30)
        #agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(10)
        #agregamos la ponderacion de la probabilidad
        self.selenium.find_element_by_name('pondProbabilidad').send_keys(20)
        # Hacemos click en agregar
        self.selenium.find_element_by_name('editar').click()
        #para las alertas del navegador
        confirmacion = self.selenium.switch_to.alert
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        #Intentamos agregar un impacto que ya se encuentra registrado
        self.selenium.find_element_by_css_selector('#agregar-estudio').click()
        #agregamos el nombre Impacto SC
        self.selenium.find_element_by_name('nombre').send_keys(nombre)
        self.selenium.execute_script("window.scrollTo(0, 720)") # movemos el scroll un poco

        # agregamos la ponderacion de la intensidad
        self.selenium.find_element_by_name('pondIntensidad').send_keys(20)

        # agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(20)

        # agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(30)

        # agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(10)

        # agregamos la ponderacion de la probabilidad
        self.selenium.find_element_by_name('pondProbabilidad').send_keys(20)


        self.selenium.find_element_by_name('editar').click() # Hacemos click en agregar
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        time.sleep(2)
        self.selenium.find_element_by_name('nombre').clear()

        # agregamos el nombre no repetido
        self.selenium.find_element_by_name('nombre').send_keys('Impacto 5')
        self.selenium.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        self.selenium.find_element_by_name('editar').click() # Hacemos click en agregar
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        #Visualizando los datos del impacto SC y modificandolos
        consulta = Estudio.objects.get(nombre=nombre)
        self.selenium.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        self.selenium.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        self.selenium.execute_script("window.scrollTo(0, 0)") #movemos el scroll un poco
        self.selenium.find_element_by_name('nombre').clear()

        #agregamos el nombre
        self.selenium.find_element_by_name('nombre').send_keys("Este es un nuevo nombre")
        self.selenium.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        self.selenium.find_element_by_name('pondExtension').clear()

        #agregamos la ponderacion de la extension
        self.selenium.find_element_by_name('pondExtension').send_keys(0)
        self.selenium.find_element_by_name('pondDuracion').clear()

        #agregamos la ponderacion de la duracion
        self.selenium.find_element_by_name('pondDuracion').send_keys(20)
        self.selenium.find_element_by_name('pondReversibilidad').clear()

        #agregamos la ponderacion de la reversibilidad
        self.selenium.find_element_by_name('pondReversibilidad').send_keys(40)
        self.selenium.find_element_by_name('editar').click() # Hacemos click en agregar
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        self.selenium.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        self.selenium.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        self.selenium.execute_script("window.scrollTo(0, 0)") #movemos el scroll un poco

        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        #Consultando los datos y Eliminando el impacto F cambiado
        nombre = "Impacto F"
        consulta = Estudio.objects.get(nombre=nombre)
        self.selenium.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        self.selenium.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        self.selenium.find_element_by_name('eliminar').click() # Hacemos click en agregar
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/index/'))

        ### Prueba a bases de calculo ###
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/modificar_tablas/'))
        self.selenium.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco

        self.selenium.find_element_by_name('valor1').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor1').send_keys("9.0")
        self.selenium.find_element_by_name('valor2').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor2').send_keys("6.0")
        self.selenium.find_element_by_name('valor6').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor6').send_keys("6.0")
        self.selenium.find_element_by_name('valor8').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor8').send_keys("1.0")
        self.selenium.find_element_by_name('valor9').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor9').send_keys("4.0")
        self.selenium.find_element_by_name('valor12').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor12').send_keys("0.0")
        self.selenium.find_element_by_name('valor13').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor13').send_keys("9.0")
        self.selenium.find_element_by_name('valor14').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor14').send_keys("6.0")
        self.selenium.find_element_by_name('valor15').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor15').send_keys("4.0")
        self.selenium.find_element_by_name('valor16').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor16').send_keys("1.0")
        self.selenium.find_element_by_name('valor17').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor17').send_keys("1.0")
        self.selenium.find_element_by_name('valor19').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor19').send_keys("8.0")
        self.selenium.find_element_by_name('valor21').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor21').send_keys("9.0")
        self.selenium.find_element_by_name('valor24').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor24').send_keys("0.0")
        self.selenium.find_element_by_name('valor27').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor27').send_keys("2.0")
        self.selenium.find_element_by_name('valor32').clear()
        confirmacion = self.selenium.switch_to.alert #para las alertas del navegador
        confirmacion.accept()
        #self.selenium.find_element_by_name('valor32').send_keys("1.0")
        self.selenium.find_element_by_name('submit').click()
        self.selenium.get('%s%s' % (self.live_server_url, '/configuracion/tablas/'))
